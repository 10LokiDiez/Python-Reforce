import csv

def studentsorder(student):
    return student["name"]

students = []
with open("CS50CODES/file/names.csv") as file:
    #lines = csv.reader(file)
    lines = csv.DictReader(file)
    for line in lines:
        #students.append({"name": line[0], "house": line[1]})
        students.append({"name": line["name"], "house": line["house"]})
        


for student in sorted(students, key=studentsorder):
    print(f"name: {student["name"]} house: {student["house"]}")