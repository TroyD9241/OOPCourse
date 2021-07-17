class Player:
    team_name = 'Bayern' # class variable

    def __init__(self, name):
        self.name = name # creating instance variable

p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
# Name: Mark
# Team Name: Liverpool
# Name: Steve
# Team Name: Liverpool

# p1 = Player('Mark')
#? p1.formerTeams.append('Barcelona') # wrong use of class variable
# p2 = Player('Steve')
#? p2.formerTeams.append('Chelsea') # wrong use of class variable
# print("Name:", p1.name)
# print("Team Name:", p1.teamName)
# print(p1.formerTeams)
# print("Name:", p2.name)
# print("Team Name:", p2.teamName)
# print(p2.formerTeams)
# Name: Mark
# Team Name: Liverpool
# ['Barcelona', 'Chelsea']
# Name: Steve
# Team Name: Liverpool
# ['Barcelona', 'Chelsea']

class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []
        #property for formerTeams is now unique for each Player Class


p1 = Player('Mark')
p1.formerTeams.append('Barcelona')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)


class Player:
    teamName = 'Liverpool'      # class variables
    teamMembers = []
    #good use of class variables

    def __init__(self, name):
        self.name = name        # creating instance variables
        self.formerTeams = []
        self.teamMembers.append(self.name)
        # will be populated by all instances of created Player class



p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Members:")
print(p1.teamMembers)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.teamMembers)
