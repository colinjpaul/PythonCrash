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

    def update_odometer(self, mileage):
        '''
        Set the odometer reading to a given value
        Reject the change if it attempts to roll back to reading
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading'''
        self.odometer_reading += miles