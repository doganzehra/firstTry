userInformation = []

name = input("Please enter your name:")
lastname = input("Please enter your lastname:")
weight = float(input("Please enter your weight:"))
height = float(input("Please enter your height:"))
bodyMassIndex = weight / (height * height)
status = None

if(bodyMassIndex < 18.5):
	status = "slim"
elif(bodyMassIndex > 18.5 and bodyMassIndex < 25):
	status = "normal"
elif(bodyMassIndex > 25 and bodyMassIndex < 30):
	status = "fat"
elif(bodyMassIndex > 30):
	status = "obese"
	
userInformation = [name,lastname,weight,height,bodyMassIndex,status]

print("User Name: {}\nUser LastName: {}\nWeight: {}\nHeight: {}\nBody Mass Index : {}\nStatus: {}\n".format(userInformation[0],userInformation[1],userInformation[2],userInformation[3],userInformation[4],userInformation[5]))

