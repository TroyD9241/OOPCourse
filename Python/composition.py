# In composition, the lifetime of the owned
# object depends on the lifetime of the owner.

class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details:", self.capacity)

class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)

class Doors:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors:", self.doors)

class Car:
    def __init__(self, engine, tires, doors, color):
        self.engineObject = Engine(engine)
        self.tireObject = Tire(tires)
        self.doorObject = Doors(doors)
        self.color = color

    def printDetails(self):
        self.engineObject.printDetails()
        self.tireObject.printDetails()
        self.doorObject.printDetails()
        print("Car Color:", self.color)


car = Car(1600, 4, 2, "Grey")
car.printDetails() #! here when car is deleted then
#! the other classes that are PART OF this class will also be deleted

# Engine Details: 1600
# Number of tires: 4
# Number of doors: 2
# Car color: Grey
