#! single inheritance

class Vehicle: #parent class
    def setTopSpeed(self, speed): #define the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle): # child class
    def openTrunk(self):
        print('Trunk is open')

corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(220)  # accessing methods from the parent class
corolla.openTrunk()  # accessing method from its own class
# Top speed is set to 220
# Trunk is now open.

#! mult-level inheritance

#? A car IS A vehicle
#? A hybrid IS A car

class Hybrid(Car): # child of car class
    def turnOnHybrid(self):
        print('Hybrid mode is on')


priusPrime = Hybrid()  # creating an object of the Hybrid class
priusPrime.setTopSpeed(220)  # accessing methods from the parent class
priusPrime.openTrunk()  # accessing method from the parent class
priusPrime.turnOnHybrid()  # accessing method from the child class
# Top speed is set to 220
# Trunk is now open.
# Hybrid mode is now switched on.

#! Hierarchical Inheritance
#? A car IS A Vehicle
#? A truck IS A vehicle

class Vehicle: #parent class
    def setTopSpeed(self, speed): # defining the set
        self.topSpeed = speed
        print('Top speed is set to', self.topSpeed)

class Car(Vehicle): # child of Vehicle
    pass

class Truck(Vehicle): # child of vehicle
    pass

corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(220)  # accessing methods from the parent class

volvo = Truck()  # creating an object of the Truck class
volvo.setTopSpeed(180)  # accessing methods from the parent class

# Top speed is set to 220
# Top speed is set to 180

#! Multiple Inheritance
#? HybridEngine IS A Electric Engine
#? HybridEngine IS A combustion engine as well

class CombustionEngine():
    def setTankCapacity(self, tankCapacity):
        self.setTankCapacity = tankCapacity

class ElectricEngine():
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# child class inherited from combustion and electric engine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print('Tank Capacity', self.setTankCapacity)
        print('Charge Capacity', self.chargeCapacity)

car = HybridEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
# Tank Capacity: 20 Litres
# Charge Capacity: 250 W

#! Hybrid Inheritance
#? combustionEngine IS A Engine
#? Electric Engine IS A engine
#? Hybrid Engine IS A electricEngine and CombustionEngine

class Engine: # parent class
    def setPower(self, power):
        self.power = power

class CombustionEngine(Engine): # child class inherited from engine
    def setTankCapacity(self, tankCapacity):
        self.setTankCapacity = tankCapacity

class ElectricalEngine(Engine): # child class inherited from parent
    def setChargeCapacity(self, chargeCapacity):
        self.setChargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine

class HybridEngine(CombustionEngine, ElectricalEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


car = HybridEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()

# Power: 2000 CC
# Tank Capacity: 20 Litres
# Charge Capacity: 250 W
