# IF NO BREAK OCCURS, THEN WE GO TO ELSE

# https://www.youtube.com/watch?v=VBokjWj_cEA

needle = 'd'
haystack = ['a', 'b', 'c', 'd']

for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else: # IF NO BREAK OCCURRED !
    print('Not Found!')
