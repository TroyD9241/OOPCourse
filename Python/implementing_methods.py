class Employee:
    # define the initialize
    def __init__(self, ID=None, salary=None, department=None):
        # self is a reference to the calling object,
        # the object to which the method or property belongs to
        #if self is not mentioned the first parameter will be treated as a reference

        self.ID = ID
        self.salary = salary
        self.department = department

        def tax(self):
            return (self.salary *0.2)

        def salaryPerDay(self):
            return (self.salary/30)

    Steve = Employee(3810,2500,"HR")

print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())

# ID = 3789
# Salary 2500
# Department: Human Resources
# Tax paid by Steve: 500.0
# Salary per day of Steve 83.33333333333333


class Employee:
    #defining the props and assinging them to none
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

        # method overloading
        #? why overloading? overloading saves you space in memory
        #? creating new mehtods is costlier
        def demo(self, a, b, c, d=5, e=None):
            print("a =", a)
            print("b =", b)
            print("c =", c)
            print("d =", d)
            print("e =", e)

        def tax(self, title=None):
            return (self.salary *.2)

        def salaryPerDay(self):
            return(self.salary / 30)


Steve = Employee()
# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")
# Demo 1
# a = 1
# b = 2
# c = 3
# d = 5
# e = None

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")
# Demo 2
# a = 1
# b = 2
# c = 3
# d = 4
# e = None

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)
# Demo 3
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
