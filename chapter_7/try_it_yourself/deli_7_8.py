sandwich_orders = ['blt', 'pastrami', 'bacon', 'chicken', 'pastrami', 'tuna', 'chicken', 'pastrami', 'beef', 'chicken',
                   'salmon', 'salad']
finished_sandwiches = []

print("\nWe've run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    for sandwich in sandwich_orders:
        finished = sandwich_orders.pop()
        finished_sandwiches.append(finished)

for sandwich in finished_sandwiches:
    print(sandwich)




