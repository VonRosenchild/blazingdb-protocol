# automatically generated by the FlatBuffers compiler, do not modify

# namespace: protocol

import flatbuffers

class NodeConnection(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNodeConnection(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NodeConnection()
        x.Init(buf, n + offset)
        return x

    # NodeConnection
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NodeConnection
    def Port(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # NodeConnection
    def Path(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # NodeConnection
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def NodeConnectionStart(builder): builder.StartObject(3)
def NodeConnectionAddPort(builder, port): builder.PrependInt32Slot(0, port, 0)
def NodeConnectionAddPath(builder, path): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(path), 0)
def NodeConnectionAddType(builder, type): builder.PrependInt8Slot(2, type, 0)
def NodeConnectionEnd(builder): return builder.EndObject()
