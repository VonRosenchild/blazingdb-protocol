# automatically generated by the FlatBuffers compiler, do not modify

# namespace: gdf

import flatbuffers

class gdf_column_handler(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsgdf_column_handler(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = gdf_column_handler()
        x.Init(buf, n + offset)
        return x

    # gdf_column_handler
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # gdf_column_handler
    def Data(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .cudaIpcMemHandle_t import cudaIpcMemHandle_t
            obj = cudaIpcMemHandle_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # gdf_column_handler
    def Valid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .cudaIpcMemHandle_t import cudaIpcMemHandle_t
            obj = cudaIpcMemHandle_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # gdf_column_handler
    def Size(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # gdf_column_handler
    def Dtype(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # gdf_column_handler
    def DtypeInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .gdf_dtype_extra_info import gdf_dtype_extra_info
            obj = gdf_dtype_extra_info()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # gdf_column_handler
    def NullCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

def gdf_column_handlerStart(builder): builder.StartObject(6)
def gdf_column_handlerAddData(builder, data): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)
def gdf_column_handlerAddValid(builder, valid): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(valid), 0)
def gdf_column_handlerAddSize(builder, size): builder.PrependUint16Slot(2, size, 0)
def gdf_column_handlerAddDtype(builder, dtype): builder.PrependInt8Slot(3, dtype, 0)
def gdf_column_handlerAddDtypeInfo(builder, dtypeInfo): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(dtypeInfo), 0)
def gdf_column_handlerAddNullCount(builder, nullCount): builder.PrependUint16Slot(5, nullCount, 0)
def gdf_column_handlerEnd(builder): return builder.EndObject()
