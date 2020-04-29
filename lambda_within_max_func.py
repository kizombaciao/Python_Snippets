x = [(1, 2), (3, 4), (1, 0)]

print(max(x, key=lambda y: y[1]))

# USING LAMBDA FUNCTION WITHIN A MAX FUNCTION
# go through the list and compare the second element
# find the one with the largest, which is 4
# and then return the tuple, which is (3, 4)