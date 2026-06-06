file = open("poems.txt", "r")

text = file.read()

if "twinkle" in text:
    print("The word 'twinkle' is present.")
else:
    print("The word 'twinkle' is not present.")

file.close()