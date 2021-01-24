print("What do you want to do?\nIf you want to see your balance select 1\nIf you want to deposit money select 2\nIf you want to withdraw money select 3\nIf you want to exit select 4\n")
int(balance) = 2000

while True:
  operation = input("Select the operation that you want to do:")
  if (operation == "1"):
    print("Your balance is:",balance)
  elif (operation == "2"):
    amount = int(print("How much money will you deposit:"))
		balance += amount 
		print("Your new balance is:",balance)
  elif (operation == "3"):
    amount = int(input("How much money will you withdraw:"))
		if(amount > balance)
		  print("Your balance is less than amount of that you want to withdraw!!!")
		else
			balance = balance - amount
			print("Your new balance is:",balance)
	elif (operation == "4")
		print("Bye")
		break
    else:
      print("Invalid operation...")
