shape =  input("Which shape do you want to know name?")

if (shape == "quadrilateral"):
    print("Please enter the edges.")
    a = int(input("first edge:"))
    b = int(input("second edge:"))
    c = int(input("third edge:"))
    d = int(input("fourth edge:"))
    
    if (a == b and a == c and a == d):
        print("square")
    elif (a == c and b == d):
        print("rectangle")
    else:
        print("quadrilateral")    
elif (shape == "triangle"):
    a = int(input("first edge:"))
    b = int(input("second edge:"))
    c = int(input("third edge:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c ):
            print("equilateral triangle")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("isosceles triangle")
        else:
            print("scalene triangle")
    else:
        print("not a triangle")     
else:
    print("invalis shape...")