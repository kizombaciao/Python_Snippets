# https://www.youtube.com/watch?v=VBokjWj_cEA

# bad way
f = open('json1.txt')
text = f.read()
for line in text.split('\n'):
    print(line)
f.close()

# better way
f = open('json1.txt')
for line in f:
    print(line)
f.close()

# best way
with open('json1.txt') as f:
    for line in f:
        print(line)
