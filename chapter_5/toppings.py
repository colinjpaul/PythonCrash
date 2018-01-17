available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepporini', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding reqeusted topping")
    else:
        print("we don't have " + requested_topping + ".")

print("\nFinished making your pizza")

