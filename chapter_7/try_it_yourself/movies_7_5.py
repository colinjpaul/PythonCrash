
age = 0
active = True

while active:
    age = input("please input you age; 'quit' to quit")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("ticket is free")
    elif age < 12:
        print("ticket is €10")
    elif age > 100:
        print("exiting")
        active = False
    else:
        print("ticket is €15")