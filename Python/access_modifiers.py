#? public attributes can be accessed inside and outside the class

class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

        def displayId(self):
            print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)
# ID: 3789
# 2500

#? private attributes can not be accessed directly from outside the class, but can be accessed inside

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary #salary is declared as a private variable

Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error
# Traceback (most recent call last):
#   File "main.py", line 9, in <module>
#     print("Salary:", Steve.__salary)
# AttributeError: 'Employee' object has no attribute '__salary'


class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary #salary is again private

    def displaySalary(self): #public method
        print('Salary:', self.__salary)
        #! because it is a public method it can also access the private variable (IE from inside of the class Salary is avaliable)

    def __displayId(self): #this is a private method (__displayId)
        print("ID:", self.ID)

Steve = Employee(3789, 2500)
Steve.displaySalary()
Steve.__displayID()  # this will generate an error
#Salary: 2500

# Traceback (most recent call last):
#   File "main.py", line 15, in <module>
#     Steve.__displayID()
# AttributeError: 'Employee' object has no attribute '__displayID'

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print(Steve._Employee__salary)  # accessing a private property
