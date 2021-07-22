x = 5  # type of x is an integer
print(type(x))

x = "Educative"  # type of x is now string
print(type(x))

# <class 'int'>
# <class 'str'>

class Dog:
    def Speak(self):
        print('Woof Woof')
        #! what matters is that the method, in this case speak, is defined in each class

class Cat:
    def Speak('Meow meow')

class AnimalSound:
    def Sound(self, animal):
        animal.Speak()
        # type of animal is not defined here
        # type of animal is determined (#?animal.)
        # when the method is called #line 27&28
sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)
# Woof woof
# Meow meow

# why it is called Duck typing?
# if a bird speaks like a duck, swims like a duck, and eats like a duck,
# that bird is a duck.

# In layman terms,
# since both the animals, dogs and cats,
# can speak like animals, they both are animals.
# This is how we have achieved polymorphism without inheritance.
