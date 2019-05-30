import pytest

@pytest.mark.skip
def test_m1():
    assert 100 + 300 == 500, "failed"


@pytest.mark.xfail
def test_m2():
    assert 100 + 300 == 200, "failed"

@pytest.mark.set1
def test_m3():
    assert 100 + 300 == 400, "failed"
