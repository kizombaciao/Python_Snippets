x = [1, 2, 3]
print(*x)

def func(*args):        # takes unlimited number of arguments
    print(args)

func(2, 3)
func(8, 9, 0)

def func2(*args, **kwargs):        
    print(args, kwargs)

func2(2, 3, a=0, b=1, c=2)