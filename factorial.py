while True:
	number = input("Number:")
	if(number == "q"):
		print("Exit")
		break
	number = int(number)
	factorial = 1
	for i in range (2 , number+1):
		factorial = factorial * i
	print("Factorial is: ",factorial)