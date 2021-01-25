sum = 0
while True:
  a = input("Please enter number:")
  if(a == "q"):
    print("exit...")
    break
  a = int(a)
  sum += a
  print("Sum:",sum)
