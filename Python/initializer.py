class Employee:
    # defining the props and assigning them None
    def __init__(self, ID, salary, department):
        #? init is shorthand for initialize :)
        # __init__ means that this is a special method that the python
        # interpretor will treat as a special case
        #! initializer is special because it does not have a return type
        #! self is the first parameter of __init__
        #! self is used to as a way to refer to the object being initialized
        self.ID = ID
        self.salary = salary
        self.department = department

Steve = Employee(3755, 2400, "IT")
#! important to initialize with all of the desired parameters
#? creating an object of the employee class with default params

# Printing properties of Steve
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)

class Employee:
    # defining the properties and assigning None to them
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee()
Mark = Employee("3789", 2500, "Human Resources")

# Printing properties of Steve and Mark
print("Steve")
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)
print("Mark")
print("ID :", Mark.ID)
print("Salary :", Mark.salary)
print("Department :", Mark.department)
