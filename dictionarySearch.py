# a better way to search through a dictionary
# https://www.youtube.com/watch?v=VBokjWj_cEA

ages = {
    'a': 1,
    'b': 2,
    'c': 3
    }

# bad way
if 'a' in ages:
    age = ages['a']
else:
    age = 'Unknown'
print('bad way: age = %s' % (age))

# good way
age = ages.get('a', 'Unknown')
print('good way: age = %s' % (age))

