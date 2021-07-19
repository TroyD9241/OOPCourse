# An elementary User class will be modeled as:

# Having a property userName
# Having a property password
# A method named login() to grant access

# Whenever a new user comes, a new object can be
# created by passing the userName
# and password to the constructor of this class.

#! A bad example of this implementation

class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

        def login(self, username, password):
            if self.username.lower() == username.lower() and self.password == password:
                print('Login Successful! ')
            else:
                print('Credentials incorrect')

Steve = User("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
Steve.password = "6789"
Steve.login("steve", "6789")


# Access Granted!
# Invalid Credentials!
#! this is the issue steve's credentials can be changed from outside
# Access Granted!


#? A good example of the above

class User:
    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if self.__username.lower() == username.lower() and self.__password == password:
            print('access granted for ', self.__username.lower(), 'with password ', self.__password
        else:
            print('invalid')
