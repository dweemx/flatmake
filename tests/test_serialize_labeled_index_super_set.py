import numpy as np
from flatmake import flatmake
from flatmake.idl.python.Dim import LabeledIndexSuperSet


def test_name():
    test_np_arr = np.array(["t", "t", "e", "e", "s", "s", "s", "t"])
    test_name = "test_liss"
    builder = flatmake.build_labeled_index_super_set(name=test_name, np_arr=test_np_arr)
    output = builder.Output()
    liss = LabeledIndexSuperSet.LabeledIndexSuperSet()
    liss_root = liss.GetRootAsLabeledIndexSuperSet(output, 0)
    name_deserialized = liss_root.Name().decode("utf-8")
    assert test_name == name_deserialized


def test_indices():
    test_np_arr = np.array(["t", "t", "e", "e", "s", "s", "s", "t"])
    test_np_t_indices = np.array([0, 1, 7])
    test_np_e_indices = np.array([2, 3])
    test_np_s_indices = np.array([4, 5, 6])
    test_name = "test_liss"
    builder = flatmake.build_labeled_index_super_set(name=test_name, np_arr=test_np_arr)
    output = builder.Output()
    liss = LabeledIndexSuperSet.LabeledIndexSuperSet()
    liss_root = liss.GetRootAsLabeledIndexSuperSet(output, 0)
    for i in range(0, liss_root.SetsLength()):
        set_deserialized = liss_root.Sets(i)
        set_name_deserialized = set_deserialized.Name().decode("utf-8")
        if "t" == set_name_deserialized:
            indices = set_deserialized.Indices().DataAsNumpy()
            assert np.array_equal(test_np_t_indices, indices)
        if "e" == set_name_deserialized:
            indices = set_deserialized.Indices().DataAsNumpy()
            assert np.array_equal(test_np_e_indices, indices)
        if "s" == set_name_deserialized:
            indices = set_deserialized.Indices().DataAsNumpy()
            assert np.array_equal(test_np_s_indices, indices)
