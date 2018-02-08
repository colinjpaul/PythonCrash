# Store information about the pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings':  ['mushrooms', 'extra cheese'],
}

print('you ordered a ' + pizza['crust'] + ' crust with ')

for topping in pizza['toppings']:
    print(topping)


