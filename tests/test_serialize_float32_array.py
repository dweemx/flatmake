import numpy as np
from flatmake import flatmake
from flatmake.idl.python.Dim import Float32bArray


def test_serialize_float32_array():
    np.random.seed(0)
    # Expoect array of float 32 bits
    np_arr = np.random.uniform(low=0, high=1, size=10).astype(np.float32)
    builder = flatmake.build_float32_array(np_arr=np_arr)
    output = builder.Output()
    fa = Float32bArray.Float32bArray()
    fa_root = fa.GetRootAsFloat32bArray(output, 0)
    np_arr_deserialized = fa_root.DataAsNumpy()
    assert np.array_equal(np_arr, np_arr_deserialized)
