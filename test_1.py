import pytest


@pytest.mark.set1
def test_file1_method1():
    x = 5
    y = 5
    assert x + 1 == 6, "The assertion error"
    assert x == y, "Test passed"


@pytest.mark.set2
def test_file1_method2():
    a = 4
    b = 4
    assert a == b, "test passed"
    assert b == a, "test failed"
