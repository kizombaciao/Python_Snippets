class Pay:
    def __init__(self, hourly_wage):
        self.hourly_wage = hourly_wage

    def __call__(self, hours_worked):
        #print(hours_worked)
        return hours_worked

pay_test = Pay(15)
print(pay_test(8))

# the instantiated object becomes a function effectively !