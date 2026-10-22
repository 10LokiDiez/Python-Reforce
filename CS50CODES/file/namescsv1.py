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

"""for student in sorted(students, key=get_name, reverse=True):
    print(f"Name: {student["name"]:10} |House:{student["house"]}")"""
    #                          funcion lambda es anonima, coje como parametro student y retorna student["name"]
for student in sorted(students, key=lambda student : student["name"]):
    print(f"Name: {student["name"]:10} |House:{student["house"]}")