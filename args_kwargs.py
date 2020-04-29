# real python
# args      for positional arguments
# kwards    for dictionary key value pairs

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo('hello')

# args:
foo('hello', 1, 2, 3)

# kwargs:
foo('hello', 1, 2, 3, key1='value', key2=999)
