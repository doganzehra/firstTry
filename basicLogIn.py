username = "zehra"
password = "4568"

usernameTemp = input("Please enter your username: ")
passwordTemp = input("Please enter your password: ")

if(username != usernameTemp and password == passwordTemp):
	print("Your username is wrong!)
elif(sername == usernameTemp and password != passwordTemp):
	print("Your password is wrong!)
elif(sername != usernameTemp and password != passwordTemp):
	print("Your informations are wrong!)
elif(sername == usernameTemp and password == passwordTemp):
	print("Entered successfully...)
else:	
	print("There is no user like that in that system.")



