# Getter mehtods allow reading a properties values
# Setters allows modifying a properties value

class User:
    def __init__(self, username=None):
        # definie the initializer
        self.__username = username

    # defining the setter
    def setUsername(self, x):
        # defining self as the value passed in as x
        self.__username = x

    # defining the getter
    def getUsername(self):
        # simply returning the private variable username
        return (self.__username)


Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())
# Before setting: steve1
# After setting: steve2
