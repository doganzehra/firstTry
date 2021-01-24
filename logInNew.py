username = "zehra" 
password  = "12345" 
numberOfLogIn = 3

while True: 
    usernameTemp = input("Please enter your username:")
    password = input("Please enter your password:")

    if (usernameTemp != username and password == password):
        print("Username is wrong")
        numberOfLogIn -= 1
        print("remaining right of entry: ", numberOfLogIn)
    elif (usernameTemp == username and password != password):
        print("Password is wrong")
        numberOfLogIn -= 1
        print("remaining right of entry: ", numberOfLogIn)
    elif (usernameTemp != username and password != password):
        print("both are wrong")
        numberOfLogIn -= 1
        print("remaining right of entry: ", numberOfLogIn)
    else:
        print("entered successfuly.")
        break
    if (numberOfLogIn == 0 ):
        print("no right to enter")
        break




