import random

def game():
    return random.randint(1,100)    # Example score

score = game()

file = open("Hi-score.txt", "r")
data = file.read()
file.close()

if data == "":
    high_score = 0
else:
    high_score = int(data)

if score > high_score:
    file = open("Hi-score.txt", "w")
    file.write(str(score))
    file.close()
    print("New High Score Updated!")
else:
    print("High Score Not Broken.")