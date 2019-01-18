class Car:
    """A sipmple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("Cars mileage is " + str(self.odometer_reading))

    def gas_range(self):
        print("Range left in tank") + str(self.gas)
        print('Cars mileage is ' + str(self.odometer_reading))

    def update_odometer(self, mileage):
        """
        Set the odometer reading to a given value
        Reject the change if it attempts to roll back to reading
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Add how much gas you filled the car with"""
        print("Filling gas")


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=70):
        """Initialise the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print statement detailing the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then Initialize attributes specific to an electric car
        """
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
my_electric_car = ElectricCar('lada', 'model x', 1975)
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()
