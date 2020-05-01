# https://www.youtube.com/watch?v=ALZmCy2u0jQ
# underscore is used to indicate private variables.

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23      # private in terms of convenience
        self.__baz = 42     # weak privacy with mangling for some protection

t = Test()
print(t)
print(dir(t))
print(t._bar)
#print(t.__baz)          # results in error because of mangling

# not recommended because the purpose is to use __baz privately inside the class !
print(t._Test__baz)     
