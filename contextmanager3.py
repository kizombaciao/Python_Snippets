# an alternative less messier way than previous version

from contextlib import contextmanager

@contextmanager
def file(fname, method):
    print('enter')
    f = open(fname, method)
    yield f
    f.close()
    print('exit')

with file('contextmanager3.txt', 'w') as f:
    print('middle')
    f.write('hello4')