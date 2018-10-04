"""Transport layer to map Flatbuffers modules with user schema classes."""

__author__ = 'BlazingDB Team'

import abc

import flatbuffers

from blazingdb.messages.blazingdb.protocol import Header, Request, Response


__all__ = ('schema', 'Schema')


def schema(module):
  """Shortcut to create concrete schema classes.

  Args:
    module: A Flatbuffers module for message

  Useful to have a simple way to define schemas.

  class ConcreteSchema(schema(FlatBuffersModule)):
    field_str = StringSegment()
    field_int = NumberSegment()
  """
  return type(module.__name__ + 'SchemaBase', (Schema,), dict(_module=module))


class MetaSchema(type):
  """Metaclass for Schema.

  To fix up segment members of the concrete schema.
  """

  def __init__(cls, name, bases, classdict):
    super(MetaSchema, cls).__init__(name, bases, classdict)
    cls._fix_up_segments()


class SchemaAttribute(abc.ABC):
  """A base class to identify schema members."""

  @abc.abstractmethod
  def _fix_up(self, cls, name):
    return NotImplemented


class Schema(metaclass=MetaSchema):
  """A class describing Flatbuffers schema.

  All classes inheriting from Schema have MetaSchema, so that segments
  are fixed up after class definition.

  class ConcreteSchema(Schema):
    _module = flatbuffer.user.message.module

    field_str = StringSegment()
    field_int = NumberSegment()

  The related flatbuffers module is `None` by default. You must override
  in parent scope in order to have working `ToBuffer` and `From` methods. See
  `schema` function as a tool to create concrete schema classes.
  """

  _segments = None
  _module = None
  _values = None
  _nested = None
  _inline = None

  def ToBuffer(self):
    builder = flatbuffers.Builder(0)

    pairs = []
    for segment in self._nested:
      pairs.append((segment._name, segment._bytes(builder, self)))

    name = self._module_name()
    getattr(self._module, name + 'Start')(builder)

    for segment in self._inline:
      pairs.append((segment._name, segment._bytes(builder, self)))

    for member, value in reversed(pairs):
      member = member[0].upper() + member[1:]
      getattr(self._module, '%sAdd%s' % (name, member))(builder, value)
    builder.Finish(getattr(self._module, name + 'End')(builder))

    return builder.Output()

  def __init__(self, **kargs):
    self._values = {}
    self._set_attributes(kargs)

  def _set_attributes(self, kargs):
    cls = self.__class__
    for name, value in kargs.items():
      segment = getattr(cls, name)
      if not isinstance(segment, Segment):
        raise TypeError('Non segment %s' % name)
      segment._set_value(self, value)

  @classmethod
  def From(cls, buffer):
    name = cls._module_name()
    obj = getattr(getattr(cls._module, name), 'GetRootAs' + name)(buffer, 0)
    members = {name: segment._from(obj)
               for name, segment in cls._segments.items()}
    name = cls._module_name()
    return type(name[0].lower() + name[1:], (), members)

  @classmethod
  def _module_name(cls):
    return _name_of(cls._module)

  @classmethod
  def _fix_up_segments(cls):
    if __name__ == cls.__module__:
      return
    cls._segments = {}
    cls._nested = []
    cls._inline = []
    for name in set(dir(cls)):
      attr = getattr(cls, name, None)
      if isinstance(attr, SchemaAttribute):
        attr._fix_up(cls, name)
        if isinstance(attr, Segment):
          cls._segments[name] = attr
          if isinstance(attr, Nested):
            cls._nested.append(attr)
          elif isinstance(attr, Inline):
            cls._inline.append(attr)
          else:
            raise TypeError('Bad `%s` segment type' % name)


class Segment(SchemaAttribute):
  """A class describing a flatbuffers object segment attribute.

  It's just a base class. To set segments for you schemas, there are specific
  subclasses for various kind of flatbuffers object attributes.

  A `Segment` subclass implementing a specific transformation between a `Schema`
  and a flutbuffers object should implement `_bytes()` of member schema and
  `_from()` flatbuffers object to DTO or literal types (like `int` or `str`).
  """

  # TODO(gcca): GenericSegment for dynamic conversion

  _name = None

  def _fix_up(self, cls, name):
    self._name = name

  @abc.abstractmethod
  def _bytes(self, builder, schema):
    return NotImplemented

  @abc.abstractmethod
  def _from(self, _object):
    return NotImplemented

  def _set_value(self, schema, value):
    schema._values[self._name] = value

  def _object_name(self):
    return self._name[0].upper() + self._name[1:]


class Nested:
  """Mark for segments with data for inside flatbuffers objs."""


class Inline:
  """Mark for segments with inline data for flatbuffers objs."""


class NumberSegment(Segment, Inline):
  """A `Segment` whose value is a literal number `int`, `float` or `bool`."""

  def _bytes(self, builder, schema):
    return schema._values[self._name]

  def _from(self, _object):
    return getattr(_object, self._object_name())()


class StringSegment(Segment, Nested):
  """A `Segment` whose value is a literal string `str`."""

  def _bytes(self, builder, schema):
    return builder.CreateString(schema._values[self._name])

  def _from(self, _object):
    return getattr(_object, self._object_name())()


class BytesSegment(Segment, Nested):
  """A `Segment` whose value is a limited sequence of `bytes`."""

  def _bytes(self, builder, schema):
    name = schema._module_name()
    member = self._object_name()
    buffer = schema._values[self._name]
    getattr(schema._module,
            '%sStart%sVector' % (name, member))(builder, len(buffer))
    for byte in reversed(buffer):
      builder.PrependByte(byte)
    return builder.EndVector(len(buffer))

  def _from(self, _object):
    name = self._object_name()
    byte = getattr(_object, name)
    return bytes(byte(i) for i in range(getattr(_object, name + 'Length')()))


class StructSegment(Segment, Inline):
  """A segment whose value is itself a flatbuffers struct as a dict.

  The keys are the flatbuffers object attributes in camelCase.
  """

  def __init__(self, module):
    self._module = module

  def _bytes(self, builder, schema):
    module = self._module
    name = _name_of(module)
    value = schema._values[self._name]
    return getattr(module, 'Create' + name)(builder, **value)

  def _from(self, _object):
    return _make_dto(getattr(_object, self._object_name())(),
                     self._name,
                     ('Init',))


class VectorSegment(Segment, Inline):

  def __init__(self, schema=None):
    self._schema = schema

  def _bytes(self, builder, schema):
    return NotImplemented

  def _from(self, _object):
    name = self._object_name()
    if self._schema and isinstance(self._schema, MetaSchema):
      no_members = ('Init', 'GetRootAs' + self._schema._module_name())
      member = getattr(_object, name)
      get = lambda i: _make_dto(member(i), self._name, no_members)
    else:
      get = getattr(_object, name)
    return (get(i) for i in range(getattr(_object, name + 'Length')()))


class SchemaSegment(Segment, Inline):

  def __init__(self, schema):
    self._schema = schema

  def _bytes(self, builder, schema):
    return NotImplemented

  def _from(self, _object):
    return _make_dto(getattr(_object, self._object_name())(),
                     self._name,
                     ('Init', 'GetRootAs' + self._schema._module_name()))


def _name_of(module):
  return module.__name__.split('.')[-1]


def _make_dto(_object, name, no_members):
  return type(name, (), {m[0].lower() + m[1:]: getattr(_object, m)()
                         for m in set(dir(_object)) - set(no_members)
                         if m[0].isalpha()})
