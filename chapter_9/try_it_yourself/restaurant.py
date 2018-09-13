class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant Name: ' + self.name)
        print('Cuisine Type: ' + self.cuisine)
        print('Customers Served: ' + str(self.number_served))

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, numbers):
        self.number_served += numbers

    def open_restaurant(self):
        print('The Restaurant is now open')


restaurant = Restaurant('Conna Cuisine', 'Traditional')
restaurant.set_number_served(17)
restaurant.increment_number_served(7)

restaurant.describe_restaurant()
restaurant.open_restaurant()