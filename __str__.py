# real python
# __str__ easy to read, for human consumption

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return 'a {self.color} car'.format(self=self)

if __name__ == "__main__":
    my_car = Car('red', 37281)
    print(my_car)
    #my_car
    #str(my_car)
    #'{}'.format(my_car)