# automatically generated by the FlatBuffers compiler, do not modify

# namespace: io

import flatbuffers

class FileSystemTableGroup(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFileSystemTableGroup(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FileSystemTableGroup()
        x.Init(buf, n + offset)
        return x

    # FileSystemTableGroup
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FileSystemTableGroup
    def Tables(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .FileSystemBlazingTable import FileSystemBlazingTable
            obj = FileSystemBlazingTable()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FileSystemTableGroup
    def TablesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FileSystemTableGroup
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def FileSystemTableGroupStart(builder): builder.StartObject(2)
def FileSystemTableGroupAddTables(builder, tables): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(tables), 0)
def FileSystemTableGroupStartTablesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FileSystemTableGroupAddName(builder, name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def FileSystemTableGroupEnd(builder): return builder.EndObject()