# automatically generated by the FlatBuffers compiler, do not modify

# namespace: orchestrator

import flatbuffers

class DMLResponse(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDMLResponse(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DMLResponse()
        x.Init(buf, n + offset)
        return x

    # DMLResponse
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DMLResponse
    def ResultToken(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # DMLResponse
    def NodeConnection(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .NodeConnection import NodeConnection
            obj = NodeConnection()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def DMLResponseStart(builder): builder.StartObject(2)
def DMLResponseAddResultToken(builder, resultToken): builder.PrependUint64Slot(0, resultToken, 0)
def DMLResponseAddNodeConnection(builder, nodeConnection): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(nodeConnection), 0)
def DMLResponseEnd(builder): return builder.EndObject()
