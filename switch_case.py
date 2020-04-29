# https://www.youtube.com/watch?v=gllUwQnYVww&list=PLP8GkvaIxJP0VAXF3USi9U4JnpxUvQXHx

# switch case method using first class functions
def dispatch_dict(op, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(op, lambda: None)()

t1 = dispatch_dict('add', 5, 3)
print(t1)

###################################
# old approach using if condition, since python doesn't provide switch case
def dispatch_if(op, x, y):
    if op == 'add':
        return x + y
    if op == 'sub':
        return x - y
    if op == 'mul':
        return x * y
    if op == 'div':
        return x / y
    return None
        
#####################################
# example of first class functions
def handle_a(x, y):
    return x + y
def handle_b(x, y):
    return x - y
def handle_default(x, y):   # default if none provided
    return x * y
func_dict = {
    'cond_a': handle_a,
    'cond_b': handle_b,
}
cond = 'cond_a'
ttt = func_dict.get(cond, handle_default)(3, 1)
print(ttt)