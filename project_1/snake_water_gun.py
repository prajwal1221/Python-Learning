'''
1= snake 
0 = water
-1 = gun

'''
import random

machine = random.choice([1, 0, -1])
youChoice = input("Enter you choice : ")
userDict = {"s": 1, "w": 0, "g": -1}
gameDict = {1: "snake", 0: "water", -1: "gun"}
You = userDict[youChoice]

print(f"You choose : {gameDict[You]}")
print(f"Machine choose : {gameDict[machine]}")

if You == machine:
    print("Draw")
else:
    if You == 1 and machine == 0:
        print("You win")
    elif You == 0 and machine == -1:
        print("You win")
    elif You == -1 and machine == 1:
        print("You win")
    else:
        print("You lose")