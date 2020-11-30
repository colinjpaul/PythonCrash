stop = False

while not stop:
    try:
        number_1 = input("input first number > ")
        number_2 = input("input second number > ")
        result = int(number_1) + int(number_2)
    except ValueError:
        print("Both numbers need to be numeric")
    else:
        print("Result is > ", result)
        go_again = input("Do you want to try again? (n) to stop?")
        if go_again == 'n' or go_again == 'N':
            stop = True







