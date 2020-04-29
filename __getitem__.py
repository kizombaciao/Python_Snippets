import copy
 
# Constants that can be used to index date of birth's Date-Month-Year
D = 0; M = 1; Y = -1            # how is this incorporated? just sub letter with number !
 
class Person(object):
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob
 
    def __getitem__(self, indx):
        print ("Calling __getitem__")
        p = copy.copy(self)
 
        p.name = p.name.split(" ")[indx]
        p.dob = p.dob[indx] # or, p.dob = p.dob.__getitem__(indx)
        return p

p = Person(name = 'Jonab Gutu', age = 20, dob=(1, 2, 1999))
print(p[0].name) # print first (or last) name
print(p[Y].dob)  # print (Date or Month or ) Year of the 'date of birth'

print(p[0].age)
print(p[0].dob)
print(p[1].dob)
print(p[-1].dob)
#print(p[2].dob)    # why doesn't index 2 work ???



# https://www.quora.com/What-is-Getitem-in-Python
# # https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
