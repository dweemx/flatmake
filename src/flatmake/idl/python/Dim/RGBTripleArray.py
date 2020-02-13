# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Dim

import flatbuffers

class RGBTripleArray(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRGBTripleArray(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RGBTripleArray()
        x.Init(buf, n + offset)
        return x

    # RGBTripleArray
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RGBTripleArray
    def R(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # RGBTripleArray
    def RAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # RGBTripleArray
    def RLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # RGBTripleArray
    def G(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # RGBTripleArray
    def GAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # RGBTripleArray
    def GLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # RGBTripleArray
    def B(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # RGBTripleArray
    def BAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # RGBTripleArray
    def BLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def RGBTripleArrayStart(builder): builder.StartObject(3)
def RGBTripleArrayAddR(builder, r): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(r), 0)
def RGBTripleArrayStartRVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def RGBTripleArrayAddG(builder, g): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(g), 0)
def RGBTripleArrayStartGVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def RGBTripleArrayAddB(builder, b): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(b), 0)
def RGBTripleArrayStartBVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def RGBTripleArrayEnd(builder): return builder.EndObject()
