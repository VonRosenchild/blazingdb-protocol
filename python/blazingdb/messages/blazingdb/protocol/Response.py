# automatically generated by the FlatBuffers compiler, do not modify

# namespace: protocol

import flatbuffers

class Response(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsResponse(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Response()
        x.Init(buf, n + offset)
        return x

    # Response
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Response
    def Status(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Response
    def Payload(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Response
    def PayloadLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ResponseStart(builder): builder.StartObject(2)
def ResponseAddStatus(builder, status): builder.PrependInt8Slot(0, status, 0)
def ResponseAddPayload(builder, payload): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(payload), 0)
def ResponseStartPayloadVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def ResponseEnd(builder): return builder.EndObject()
