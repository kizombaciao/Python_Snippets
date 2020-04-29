# note, context manager is not just for opening files, but also for threads and open/close database
# think of situation where context manager is useful, allowing python to handle closing of resources

# https://www.youtube.com/watch?v=Lv1treHIckI
# https://www.youtube.com/watch?v=C-gEQdGVXbk


f = open('file.txt', 'w')
try:
    f.write('hello\n')
finally:
    f.close()

########################

with open('contextmanager.txt', 'a') as f:
    f.write('hello2')

