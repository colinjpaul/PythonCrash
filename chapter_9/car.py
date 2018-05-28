class Car():
    '''A sipmple attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('Cars mileage is ' + str(self.odometer_reading))

my_new_car = Car('Audi', 'A4', 2018)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()