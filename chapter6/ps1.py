a = int(input("Enter a number 1: "))

b = int(input("Enter a number 2: "))

c = int(input("Enter a number 3: "))

d = int(input("Enter a number 4: "))

if (a>b and a>c and a>d):
    print ("no 1 is bigger ")
elif (b>a and b>c and b>d):
    print ("no 2 is bigger ")
elif (c>a and c>b and c>d):
    print ("no 3 is bigger ")
else:    print ("no 4 is bigger ")