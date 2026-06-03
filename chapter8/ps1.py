# code for greatest of three number using functions

def greatest(a , b , c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
    
a = int(input("Enter 1st Number :"))
b = int(input("Enter 2nd Number :"))
c = int(input("Enter 3rd Number :"))


print(greatest(a , b , c))