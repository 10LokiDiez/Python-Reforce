with open("CS50CODES/file/names.txt", "r") as file:
    lines = file.readlines()
"""names = []
with open("CS50CODES/file/names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())"""
for line in sorted(lines, reverse=True):
    print(f"hello, {line.rstrip()}")