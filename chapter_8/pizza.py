def make_pizza(size, *toppings):
    '''Summarise the pizza we are making'''
    print("\nMaking a " + str(size) +
          " inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)