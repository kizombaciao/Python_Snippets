import pickle

class Fruit:
    def __init__(self, name):
        self.name = name
        if name == "banana":
            self.color = "yellow"
        else:
            self.color = "unknown"

myfruit = Fruit("banana")
pickle.dump(myfruit, file=open("test.pkl", "wb"))
del myfruit
myfruit = pickle.load(file=open("test.pkl", "rb"))
print(myfruit.color)