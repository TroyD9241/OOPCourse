# Employee Class
# properties
# ID, Salary, Department

class Employee:
    # defining the properties and assigning them to none
    ID = None
    salary = None
    department = None
    #! python code will not compile if you do not initialize the values of properties
    #! IE...ID = None...OK
    #! ...ID...Not Okay

Steve = Employee()
# instantiating a new Employee class object name Steve

Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
#? assigning values to the properties of Steve

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
# ID = 3789
# Salary 2500
# Department: Human Resources
#! This is 1) way to assign values to props..

# class Employee:
#     # defining the properties and assigning them to none
#     ID = 3789
#     salary = 2500
#     department = "Human Resources "
#     #? 2) assign the values in the main code

Steve.title = 'Manager'
# creates a new attribute for Steve

print('Title', Steve.title)
#Title: Manager
