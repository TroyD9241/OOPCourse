# Aggregation follows the Has-A model, which creates a parent-child relationship
# between two classes with one class owning the object of another

#? Aggregated Objects do not depend on the lifetime of their owners

class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population =population

    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population", self.population)

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()

C = Country("Wales", 1500)
p = Person("Joe", c)
p.printDetails()
# Person Name: Joe
# Country Name: Wales
# Country Population 1500

#deletes the object P
del p
print("")
c.printDetails()

# Country Name: Wales
# Country Population 1500
