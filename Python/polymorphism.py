
#! poor example of polymorphism

class Rectangle():

    #initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

        #method to calculate area

    def getArea(self):
        return self.width * self.height

class Circle():
    #initializer
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    #method to calculate area

    def getArea(self):
        return self.radius * self.radius * 3.142


shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))
# Sides of a rectangle are 4
# Area of rectangle is: 60
# Sides of a circle are 0
# Area of circle is: 153.958

#! good example of polymorphism using inheritance

class Shape:
    def __init__(self):
        self.sides = 0

    def getArea(self):
        pass

class Rectangle(Shape):
    #initializer
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sides = 4

    #method to calculate area
    def getArea(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.sides = 0

    def getArea(self):
        return self.radius * self.radius * 3.142
