class Animal:
    # parent class
    def __init__(self, name, sound):
        # initializer
        self.name = name
        self.sound = sound
        # properties

    def Animal_details(self):
        print ("Name:", self.name)
        print("Sound:", self.sound)
        #method

class Dog(Animal):
    # child class inherits from Animal
    def __init__(self, name, sound, family):
        # calls the init function from the parent class
        super().__init__(name, sound)
        # new prop family
        self.family = family

    def Animal_details(self):
        # overridden method
        super().Animal_details()
        # calls teh parent method
        print("Family:", self.family)
        # prints family

class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):
        super().Animal_details()
        self.color = color

d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print("")
s = Sheep("Billy", "Baa Baa", "White")
s.Animal_details()

# Name: Pongo
# Sound: Woof Woof
# Family: Husky

# Name: Billy
# Sound: Baa Baa
# Color: White
