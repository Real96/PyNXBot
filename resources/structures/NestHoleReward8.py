# automatically generated by the FlatBuffers compiler, do not modify

# namespace: structures

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class NestHoleReward8(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNestHoleReward8(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NestHoleReward8()
        x.Init(buf, n + offset)
        return x

    # NestHoleReward8
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NestHoleReward8
    def EntryID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleReward8
    def ItemID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleReward8
    def Values(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # NestHoleReward8
    def ValuesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # NestHoleReward8
    def ValuesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NestHoleReward8
    def ValuesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def NestHoleReward8Start(builder): builder.StartObject(3)
def NestHoleReward8AddEntryID(builder, EntryID): builder.PrependUint32Slot(0, EntryID, 0)
def NestHoleReward8AddItemID(builder, ItemID): builder.PrependUint32Slot(1, ItemID, 0)
def NestHoleReward8AddValues(builder, Values): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(Values), 0)
def NestHoleReward8StartValuesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def NestHoleReward8End(builder): return builder.EndObject()