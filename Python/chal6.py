# Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

        def getBalance(self):
            return self.balance

        def deposit(self, amount):
            self.balance = self.balance + amount

        def withdrawl(self, amount):
            self.balance = self.balance - amount

class SavingsAccount(Account):
    # __init__ is the Initializer!
    def __init__(self, title=None, balance=0, interestRate=0):
        # super calls the initializer in the parent class
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate / 100)
