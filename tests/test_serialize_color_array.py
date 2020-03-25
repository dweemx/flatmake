import numpy as np
from flatmake import flatmake
from flatmake.idl.python.Dim import ColorArray1D


def test_serialize_color_array():
    np.random.seed(0)
    np_arr = np.random.randint(0, 10, 10)
    np_arr_normalized = flatmake.normalize_to_rgb(
        np_arr=np_arr
    )
    builder = flatmake.build_color_array(
        np_arr=np_arr_normalized
    )
    output = builder.Output()
    ca1d = ColorArray1D.ColorArray1D()
    ca1d_root = ca1d.GetRootAsColorArray1D(output, 0)
    np_arr_deserialized = ca1d_root.Color().DataAsNumpy()
    assert np.array_equal(np_arr_normalized, np_arr_deserialized)
