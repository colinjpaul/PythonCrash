class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 17

    def describe_restaurant(self):
        print('Restaurant Name: ' + self.name)
        print('Cuisine Type: ' + self.cuisine)
        print('Customers Served: ' + str(self.number_served))

    def open_restaurant(self):
        print('The Restaurant is now open')


restaurant = Restaurant('Conna Cuisine', 'Traditional')
restaurant.describe_restaurant()

