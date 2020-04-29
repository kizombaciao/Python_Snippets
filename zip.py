names = ['a', 'b', 'c']
ages = [1, 2, 3, 4]     # note, 4 is omitted!
fav_color = ['b', 'r', 'g']

print(list(zip(names, ages, fav_color)))

for tup in zip(names, ages, fav_color):
    print(tup)

for name, age, color in zip(names, ages, fav_color):
    print(name, age, color)