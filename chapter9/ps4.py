file = open("sample.txt", "r")

text = file.read()

file.close()

text = text.replace("Donkey", "#####")

file = open("sample.txt", "w")

file.write(text)

file.close()

print("Word replaced successfully.")