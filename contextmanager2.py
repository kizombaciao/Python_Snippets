
class File:
    def __init__(self, filename, method):
        self.f = open(filename, method)

    # note, enter and exit both get called, despite no explicit calls !
    def __enter__(self):
        print('Enter')
        return self.f

    def __exit__(self, type, value, traceback):
        print(f"{type}, {value}, {traceback}") # ???
        print('Exit')
        self.f.close()
        if type == Exception:
            return True # if we successfully close 'f', then no exception raised !

with File('contextmanager2.txt', 'w') as f:
    print('middle')
    f.write('hello3')
    raise Exception()
    # note, that exception was raised after Exit !
