midterm1 = int(input("Please enter first midterm grade: "))
midterm2 = int(input("Please enter second midterm grade: "))
final = int(input("Please enter final grade: "))

totalGrade = midterm1 * 0.3 + midterm2 * 0.3 + final * 0.4

if(totalGrade >= 90):
	print("AA")
elif(totalGrade >= 85):
	print("BA")
elif(totalGrade >= 80):
	print("BB")
elif(totalGrade >= 75):
	print("CB")
elif(totalGrade >= 70):
	print("CC")
elif(totalGrade >= 65):
	print("DC")
elif(totalGrade >= 60):
	print("DD")
elif(totalGrade >= 55):
	print("FD")
else:
	print("FF")
