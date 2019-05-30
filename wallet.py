class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount
        print("Amount is in account",self.balance)

    def add_cash(self, amount):
        self.balance += amount
        print("total amount is",self.balance)

w = Wallet(100)
w.spend_cash(110)
w.add_cash(100)