# Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.

#parent class
class Account:
    def __init__(self, title=None, balance=0):
        # this is our initializer
        self.title = title
        self.balance = balance
        # these are instance variables

        #getter that returns the balance
        def getBalance(self):
            return self.balance
        #adds to the balance
        def deposit(self, amount):
            self.balance = self.balance + amount
        # removes from the amount
        def withdrawl(self, amount):
            self.balance = self.balance - amount
        # these are instance methods
class SavingsAccount(Account):
    # __init__ is the Initializer!
    def __init__(self, title=None, balance=0, interestRate=0):
        # super calls the initializer in the parent class
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate / 100)
