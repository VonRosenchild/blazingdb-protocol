# automatically generated by the FlatBuffers compiler, do not modify

# namespace: gdf

import flatbuffers

class cudaIpcMemHandle_t(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAscudaIpcMemHandle_t(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = cudaIpcMemHandle_t()
        x.Init(buf, n + offset)
        return x

    # cudaIpcMemHandle_t
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # cudaIpcMemHandle_t
    def Reserved(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # cudaIpcMemHandle_t
    def ReservedLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def cudaIpcMemHandle_tStart(builder): builder.StartObject(1)
def cudaIpcMemHandle_tAddReserved(builder, reserved): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(reserved), 0)
def cudaIpcMemHandle_tStartReservedVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def cudaIpcMemHandle_tEnd(builder): return builder.EndObject()
