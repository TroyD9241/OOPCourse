# Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

a1 = Account("Mark", 5000)
