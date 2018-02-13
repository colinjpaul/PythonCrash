
message = ""
while message != 'quit':
    prompt = "\n enter a pizza topping"
    prompt += "\n type quit"
    message = input(prompt)
    if message == 'quit':
        break
    print("you entered " + message)




