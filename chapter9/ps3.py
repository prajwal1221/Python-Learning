for i in range(2, 21):
    file = open(f"tables/table_{i}.txt", "w")

    for j in range(1, 11):
        file.write(f"{i} x {j} = {i*j}\n")

    file.close()

print("Tables created successfully.")