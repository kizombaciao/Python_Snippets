# https://www.youtube.com/watch?v=CZ8bZPqtwU0&list=PLP8GkvaIxJP0VAXF3USi9U4JnpxUvQXHx&index=2

a = [1, 2, 3]
b = a
# a and b both point to the same memory


c = list(a)

# c points to a different memory
print(a == b)
print(a is b)
print(a == c) # content is the same
print(a is c) # memory location is different !

