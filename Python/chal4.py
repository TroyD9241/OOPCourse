# Problem statement #
# You are given a partially completed code of a Rectangle class in the editor. Implement the class by completing the tasks below.

# Task 1 #
# Implement a constructor to initialize the values of two private properties: length and width.

# Task 2 #
# Implement a method, area(), in the Rectangle class that returns the product of length and width. See the formula below:

# Area = length \times widthArea=length×width

class Rectangle:
    def __init__(self, length=None, width=None):
        # defined our initializer
        self.__length = length

        self.__width = width
        # declared our variables as PRIVATE so they can NOT be modified directly
    def area(self):
        area = self.__length * self.__width
        # this public method modifies values
        return area

    def perimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        return perimeter
