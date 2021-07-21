class Shape:
    def __init__(self):
        self.sides = 0

    def getArea(self):
        pass

class Rectangle(Shape): # derived from shape class
    #initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    #method to get area
    def getArea(self):
        return self.width * self.height

class Circle(Shape): # derived from shape
    def __init__(self, radius=0):
        self.radius = radius

    def getArea(self):
        return self.radius * self.radius * 3.142

shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))
# Area of rectangle is: 60
# Area of circle is: 153.958
