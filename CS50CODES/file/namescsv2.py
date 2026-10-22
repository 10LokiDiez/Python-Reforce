import csv
students = []
with open("CS50CODES/file/names.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name":row[0], "house":row[1]})

def get_name(student):
    return student["name"]
    

"""for student in sorted(students, key=get_name, reverse=True):
    print(f"Name: {student["name"]:10} |House:{student["house"]}")"""
    #                          funcion lambda es anonima, coje como parametro student y retorna student["name"]
for student in sorted(students, key=lambda student : student["name"]):
    print(f"Name: {student["name"]:10} |House:{student["house"]}")