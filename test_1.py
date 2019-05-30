import pytest
from wallet import Wallet, InsufficientAmount



def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_add_cash_total_amount():
    wallet = Wallet(100)
    wallet.add_cash(50)
    assert wallet.balance == 150

def test_spend_cash_total_amount():
    wallet = Wallet(100)
    wallet.spend_cash(50)
    assert wallet.balance == 50

def test_exception_spend_cash_total_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
         wallet.spend_cash(100)