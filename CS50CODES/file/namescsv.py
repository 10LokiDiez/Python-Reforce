import csv
students = []
with open("CS50CODES/file/names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #student = {"name": name, "house":house}
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"Name: {student["name"]:10} |House:{student["house"]}")