# Task 1 #
# Implement a constructor to initialize the values of four properties: name, phy, chem, and bio.

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio


# Task 2 #
# Implement a method – totalObtained – in the Student class that calculates total marks of a student.
    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def percentage(self):
        return((self.totalObtained() / 300) * 100)



Mark = Student('Mark', 80, 90, 40)
print(Mark.name)
print(Mark.totalObtained())
print(Mark.percentage())

# Task 3 #
# Using the totalObtained method, implement another method, percentage,
# in the Student class that calculates the percentage of students marks.
# Assume that the total marks of each subject are 100. The combined marks of three subjects are 300.

# The formula for calculating the percentage is given below.
