from deepequal import deep_equal


def test_nested():
    assert deep_equal({"a": [1, {"b": 2}]}, {"a": [1, {"b": 2}]})
    assert not deep_equal({"a": 1}, {"a": 2})
