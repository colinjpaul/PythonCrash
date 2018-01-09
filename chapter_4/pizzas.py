pizzas = ['bacon', 'chicken', 'beef']

for pizza in pizzas:
    print("I like " + pizza)

print("pizza is good")

friends_pizzas = pizzas[:]
friends_pizzas.append("cheese")

for pizza in pizzas:
    print("I like " + pizza)

for pizza in friends_pizzas:
    print("Friend likes " + pizza)

