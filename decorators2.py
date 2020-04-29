# https://www.youtube.com/watch?v=bCQDdA84aCo
# also maintains the 'single responsibility principle' for functions
# including use of *args, **kwargs

from datetime import datetime
def timeit(arg):
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):
            st = datetime.now()
            res = func(*args, **kwargs)
            print(datetime.now() - st)
            return res
        return wrapper      # note, no () !
    return outer

@timeit('hello1')
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit('hello2')
def two(n):
    l = [i for i in range(n) if i % 2 == 0]
    return l

l1 = one(10000)
l2 = two(20000)
