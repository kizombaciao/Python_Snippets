# howcode youtube channel

def check(func):
    def inside(a, b):
        if b == 0:
            print("Can't divide by 0")
            return
        func(a, b)
    return inside

@check
def div(a, b):
    return a / b

# equivalent to:
#div = check(div)

print(div(10, 0))
print(div(2, 2))       # ??? this line doesn't work
