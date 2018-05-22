class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print('Restaurant Name: ' + self.name)
        print('Cuisine Type: ' + self.cuisine)

    def open_restaurant(self):
        print('The Restaurant is now open')


restaurant1 = Restaurant('Ashy Pally', 'Mexican')
restaurant2 = Restaurant('Conna', 'Italian')
restaurant3 = Restaurant('Dennys', 'Traditional')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()




