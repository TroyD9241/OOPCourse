#ABC or Abstract Base Class

# Abstract base classes define a set of methods
# and properties that a class must implement
# in order to be considered a duck-type instance of that class.

class Shape(self):
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return self.length * 4

shape = Shape()
square = Square(4)

from abc import ABC, abstractclassmethod, abstractmethod

class ParentClass(ABC):
    # use the decorator above the method you want to declare as abstract
    @abstractmethod
    def method(self)

class Shape(ABC): # shape is a child class of ABC

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

shape = Shape()
# this code will not compile since Shape has abstract methods without
# method definitions in it

class Shape(ABC): # shape is a child class of ABC
    @abstractmethod
    def area(self):
        # Note: Methods with
        # @abstractmethod decorators must be defined in the child class.
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

shape = Shape()
