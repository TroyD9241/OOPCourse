# Implement the following properties as private:

# name
# rollNumber
# Include the following methods to get and set the private properties above:

# getName()
# setName()
# getRollNumber()
# setRollNumber()
# Implement this class according to the rules of encapsulation.

#! setvalue using getter and setters
# class Student():
#     def __init__(self, name=None, rollNumber=None):
        #? this is redundant
#         self.__name = name
#         self.__rollNumber = rollNumber

#     def getName(self):
#         return self.__name
#     def setName(self, newName):
#         self.__name = newName

#     def getRollNumber(self):
#         return self.__rollNumber
#     def setRollNumber(self, newRollNumber):
#         self.__rollNumber = newRollNumber
#! Do not do this!
#? do this :)
class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber
