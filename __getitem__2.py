# THIS IS A BETTER EXAMPLE TO UNDERSTAND __GETITEM__()
# https://www.youtube.com/watch?v=JaZ3I6ev3NE
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []       # GOAL IS HOW DO SEE THESE VALUES IN THIS LIST !!! USE __GETITEM__ !

    def __len__(self):
        return len(self.players)

    def __getitem__(self, i):
        return self.players[i]

    def __repr__(self):
        return "Club {}: {}".format(self.name, len(self))


arsenal = Club("Arsenal")
arsenal.players.append("p1")
arsenal.players.append("p2")

print(arsenal[0])
print(arsenal[-1])

print(arsenal)      # calls __repr__ method !
# IF WE DIDN'T HAVE THE __REPR__ METHOD DEFINED, THEN WE GET THE MEMORY ADDRESS OF THE INSTANCE !
