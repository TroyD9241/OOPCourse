# defining the parent
class Vehicle:
    fuelCap = 90


class Car(Vehicle): # defining the child class
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle class using super()

        print("Fuel cap from the vehicle class using super", super().fuelCap)

        # accessing fuelCap from the car class using self
        print('Fuel cap from the Car Class', self.fuelCap)

obj1 = Car() # creating a car object
obj1.display() # calling the car class method display
# Fuel cap from the Vehicle Class: 90
# Fuel cap from the Car Class: 50


class Vehicle: # defining the parent class
    def display(self): #defining the display method in the parent
        print('I am from the vehicle class')

class Car(Vehicle): # define the child class
    # defining the display method in the child class
    def display(self):
        super().display()
        print('I am from the car class')

obj1 = Car() # creating car object
obj1.display() # call the car class method.

# I am from the Vehicle Class #
# I am from the Car Class # both are called from the display method in vehicle


class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b) # changing these lines does not affect
        self.c = c # changing these lines does not affect the code
        #! this allows users to manipulate parameters before passing them into the parent class


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
# 1
# 2
# 3


#? with super
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__ (self, make, color, model, doors):
        super().__init__(make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print('Name:', self.doors)

obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()
# Manufacturer: Suzuki
# Color: Grey
# Model: 2015
# Name: 4

#? without super
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Door:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()
# Manufacturer: Suzuki
# Color: Grey
# Model: 2015
# Door: 4

#! nothing changes but super makes the code more managable
