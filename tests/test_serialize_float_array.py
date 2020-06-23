import numpy as np
from flatmake import flatmake
from flatmake.idl.python.Dim import FloatArray


def test_serialize_float_array():
    np.random.seed(0)
    # Expoect array of float 32 bits
    np_arr = np.random.uniform(low=0, high=1, size=10).astype(np.float32)
    builder = flatmake.build_float_array(
        np_arr=np_arr
    )
    output = builder.Output()
    fa = FloatArray.FloatArray()
    fa_root = fa.GetRootAsFloatArray(output, 0)
    np_arr_deserialized = fa_root.DataAsNumpy()
    assert np.array_equal(np_arr, np_arr_deserialized)
