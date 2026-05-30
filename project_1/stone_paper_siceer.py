'''
1= stone 
0 = paper
-1 = siceer

'''
import random

machine = random.choice([1, 0, -1])
youChoice = input("Enter you choice : ")
userDict = {"s": 1, "p": 0, "sc": -1}
gameDict = {1: "stone", 0: "paper", -1: "siceer"}
You = userDict[youChoice]

print(f"You choose : {gameDict[You]}")
print(f"Machine choose : {gameDict[machine]}")


if You == machine:
    print("Draw")
else:
    if You == 0 and machine == 1:
        print("You win")
    elif You == 1 and machine == -1:
        print("You win")
    elif You == -1 and machine == 0:
        print("You win")
    else:
        print("You lose")