responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name")
    response = input("\nwhere in the world would you most like to go")

    responses[name] = response

    repeat = input("would you like to let another person respond? (yes/no")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + ' would like to go to ' + response)