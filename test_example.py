import pytest
# import PyTest.Cal_File as a

@pytest.mark.set1
def test_file2_method1():
    x = 5
    y = 5
    assert x  == 5, "The assertion error"
    assert x == y, "test pass"
    # AssertionError : "test failed"

@pytest.mark.set2
def test_file2_method2():
    x = 5
    y = 5
    assert x  == 5, "The assertion error"
    assert x == y, "test pass"


test_file2_method1()
test_file2_method2()