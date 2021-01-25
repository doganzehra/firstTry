def perfect():
  a = int(input("Please enter the number you want:"))
  i = 1
  sum = 0
  while(i < a):
    if(a % i == 0):
      sum += i
    i += 1
  if(sum == a):
    print(a," is a perfect number")
  else:
    print(a," is not a perfect number")
perfect()
