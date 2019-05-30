import pytest


@pytest.fixture
def supply_AA_BB_CC():
    a = 25
    b = 35
    c = 45
    return [a,b,c]

def test_comparewithA(supply_AA_BB_CC):
       z = 35
       assert supply_AA_BB_CC[0] == z, "A compare with Z failed" 

def test_comparewithBB(supply_AA_BB_CC):
	zz=35
	assert supply_AA_BB_CC[1]==zz,"bb and zz comparison failed"

def test_comparewithCC(supply_AA_BB_CC):
	zz=35
	assert supply_AA_BB_CC[2]==zz,"cc and zz comparison failed"