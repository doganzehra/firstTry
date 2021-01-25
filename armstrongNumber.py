a = input("Please enter the number you want:")
numberOfDigits = len(a)
a = int(a)
digit = 0
sum = 0
number = a
while (number > 0):
    digit = number % 10
    sum += digit ** numberOfDigits
    number //= 10

if (sum == number):
    print(number,"is a armstrong number.")
else:
    print(number,"is not a armstrong number.")