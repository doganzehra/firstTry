a = int(input("Please enter first number:")) 
b = int(input("Please enter second number:")) 

print("For addition select 1\nFor subtract select 2\nFor multiplication select 3\nFor division select 4\n")

operation =  input("Please enter the operation number:") 

if (operation == "1"):
    print("{} + {} = {}".format(a , b , a + b))
elif (operation == "2"):
    print("{} - {} = {}".format(a , b , a - b))
elif (operation == "3"):
    print("{} x {} = {}".format(a , b , a * b))
elif (operation == "4"):
    print("{} / {} = {}".format(a , b , a / b))
else:
    print("Invalid operation!")
