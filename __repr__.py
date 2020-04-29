# real python
# NOT AN USEFUL EXAMPLE

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'

if __name__ == "__main__":
    my_car = Car('red', 37281)
    print(my_car)
    '{}'.format(my_car)
    my_car
    repr(my_car)
