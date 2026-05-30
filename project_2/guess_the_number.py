import random

n = random.randint(1, 100)
a = -1 
guess = 0

while(a != n):
    a = int(input("guess the number between 1 and 100: "))
    if (a < n):
        print("the number is higher")
        guess += 1
    elif(a > n ):
        print("the number is lower")
        guess += 1

print (f"the number is {n} and you guessed it in {guess} attempts")

#store hightscore in a file without try and except
with open("highscore.txt", "r") as f:
    highsc = int(f.read())


if highsc > guess:
        with open("highscore.txt", "w") as f:
             f.write(str(guess))
        print("you have a new highscore")
else:
        print("you did not beat the highscore")
