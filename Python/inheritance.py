class ParentClass:
    #attributes of the parent class
    pass

# inherates from parentClass
class ChildClass(ParentClass):
    # attributes of the child class
    pass

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
        # calling the contructor from the parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print('Doors:', self.doors)

obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()
