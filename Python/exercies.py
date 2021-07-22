# create a vehicle class with max_speed and mileage attributes

class Vehicle:
    def __init__(self, max_speed=0, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)

#OOP Exercise 2: Create a Vehicle class without any variables and methods

class Vehicle:
    pass

# OOP Exercise 3: Create a child class Bus that will inherit
# all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def displayInfo(self):
        print('name', self.name)
        print("max speed:", self.max_speed)
        print("mileage:", self.mileage)


# OOP Exercise 4: Class Inheritance

# Create a Bus class that inherits from the Vehicle class. Give the capacity
# argument of Bus.seating_capacity() a default value of 50.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity ):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
