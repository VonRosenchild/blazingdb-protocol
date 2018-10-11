# automatically generated by the FlatBuffers compiler, do not modify

# namespace: interpreter

import flatbuffers

class GetResultResponse(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGetResultResponse(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GetResultResponse()
        x.Init(buf, n + offset)
        return x

    # GetResultResponse
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GetResultResponse
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .BlazingMetadata import BlazingMetadata
            obj = BlazingMetadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GetResultResponse
    def FieldNames(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # GetResultResponse
    def FieldNamesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GetResultResponse
    def Values(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from blazingdb.messages.blazingdb.protocol.gdf.gdf_column_handler import gdf_column_handler
            obj = gdf_column_handler()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GetResultResponse
    def ValuesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def GetResultResponseStart(builder): builder.StartObject(3)
def GetResultResponseAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def GetResultResponseAddFieldNames(builder, fieldNames): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fieldNames), 0)
def GetResultResponseStartFieldNamesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GetResultResponseAddValues(builder, values): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(values), 0)
def GetResultResponseStartValuesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GetResultResponseEnd(builder): return builder.EndObject()
