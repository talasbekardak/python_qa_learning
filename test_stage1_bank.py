import pytest

from stage0_task3 import BankAccount

def test_deposit():
    acc=BankAccount(0)
    acc.deposit(100)
    assert acc.balance() == 100
def test_withdraw():
    acc=BankAccount(0)
    acc.deposit(100)
    acc.withdraw(30)
    assert acc.balance() == 70
def test_withdraw_insufficient():
    with pytest.raises(ValueError):
        acc=BankAccount(0)
        acc.withdraw(5)