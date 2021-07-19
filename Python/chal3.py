# Problem statement #
# Write a Python class called Calculator by completing the tasks below:

# Task 1 #
# Initializer #
# Implement an initializer to initialize the values of num1 and num2.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

# Task 2 #
# Methods #
# add() is a method that returns the sum of num1 and num2.

# subtract() is a method that returns the subtraction of num1 from num2.

# multiply() is a method that returns the product of num1 and num2.

# divide() is a method that returns the division of num2 by num1.
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
       return self.num2 / self.num1
