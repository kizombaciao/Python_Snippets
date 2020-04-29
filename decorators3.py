# https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Object-Oriented/6-property-decorator/oop.py

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # allows you to define it as a method but use it like an attribute !!!
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer" # uses the setter !!!

print(emp_1.first)
print(emp_1.email) # note, i don't need email() since i can use it like an attribute !!!
print(emp_1.fullname)

del emp_1.fullname # uses the deleter !!!

# the decorator is handy because we don't want the people who have already written their code to rewrite the code,
# that's why with a decorator, the code doesn't need to be modified and we get what we want