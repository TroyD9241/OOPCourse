print(5 + 3)  # adding integers using '+'
print("money" + "maker")  # merging strings using '+'
# 8
# moneymaker

#! implement a class that represents a complex number

# A complex number consists of a real part and an imaginary part.
# z = x + iy
# z = complex, x is the real part, and y is imaginary

#example
#? a = 3 + 7i
#? b = 2 + 5i
#? a + b = (3+2) + (7+5)i = 5 + 12i
#? a - b = (3-2) + (7-5)i = 1 + 2i

class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other): # overloading the '+' operator
        # other is a reference to the other objects that are interacting with the class object
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other): # overloading the - operator
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp

obj1 = Com(3, 7)
obj2 = Com(2, 5)
#! the operator is called on obj1  obj2 is considered the other object
obj3 = obj1 + obj2 #! returned object will be stored in obj3
obj4 = obj1 - obj2 #! this line is the reverse of the above line

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imag)
# real of obj3: 5
# imag of obj3: 12
# real of obj4: 1
# imag of obj4: 2


#? common overloaded operators
# +, __add__(self, other)
# -, __sub__(self, other)
# /, __truediv__(self, other)''
# *, __mul__(self, other)
# <, __lt__(self, other)
# >, __gt__(self, other)
# ==, __eq__(self, other)
