name = input("Insert a name: ")
with open("CS50CODES/file/names.txt", "a") as file:
    file.write(f"{name}\n")