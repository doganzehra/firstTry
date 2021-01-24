"""
2. dereceden bir bilinmeyenli denklemin köklerini bulun

Denklem:ax^2 + bx + c

Delta:b ** 2 -  4 * a * c

Birinci Kök:(-b - delta ** 0.5)/(2*a)
İkinci Kök:(-b + delta ** 0.5)/(2*a)
"""

a=int(input("Please enter the value of a:"))
b=int(input("Please enter the value of b:"))
c=int(input("Please enter the value of c:"))
numberOfDelta=(b**2)-4*a*c
x1=(-b - delta ** 0.5)/(2*a)
x2=(-b + delta ** 0.5)/(2*a)
print("First root:{} , Second root:{}".format(x1,x2))





