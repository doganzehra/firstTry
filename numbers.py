a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
a,b = b,a
print("First number is: {}\nSecond number is: {}".format(a,b))
biggestNumber = None

if(a < b):
	biggestNumber = b
else:
	biggestNumber = a
print("The biggest number is {}".format(biggestNumber))