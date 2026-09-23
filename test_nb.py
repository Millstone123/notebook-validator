from nb.checker import check_notebooks


def test_sample_notebooks():
    assert check_notebooks("notebooks") == []
