# https://www.youtube.com/watch?v=C-gEQdGVXbk
# how we can populate an instance of an object with data from a dictionary, by using setattr
# and then to print out the recorded data, by using getattr

class Person():
    pass

p = Person()
p_info = {'first': 'C', 'last': 'S'}
for key, value in p_info.items():
    setattr(p, key, value)

for key in p_info.keys():
    print(getattr(p, key))

#########################
class Person():
    pass

p = Person()
first_key = 'key'
first_val = 'val'
setattr(p, first_key, first_val)
first = getattr(p, first_key)
print(first)