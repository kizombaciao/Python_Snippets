
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

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