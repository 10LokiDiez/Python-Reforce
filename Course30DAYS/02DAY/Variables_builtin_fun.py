#https://docs.python.org/es/3.14/builtins/functions.html
#Documentacion oficial de las funciones builtin
#help("keywords")
#Aqui estan las funciones

"""
Los nombres de variables distinguen mayúsculas de minúsculas (firstname, Firstname, FirstName y FIRSTNAME son variables diferentes)

_for # es si queremos usar una pablabra reservada como una variable
_if

snake_case para variables
"""
print('Hello',',', 'World','!')

first_name = "Simon"
last_name = "Diez"
full_name = first_name + " " + last_name
country = "United States of America"
city = "Miami"
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = False
day, month, month_label = 1, 10, "October"

list_of_variables = [first_name,last_name,full_name,country,city,age,year,is_married,is_true,
                     is_light_on,day,month,month_label]

for variable in list_of_variables:
    print(f"{type(variable)}, ", end="")
print()

num_one, num_two = 5, 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one **  num_two
floor_division = num_one //  num_two

operations = [total,diff,product,division,remainder,exp,floor_division]

for operation in operations:
    print(operation)
    
    
radio = int(input("QUE RADIO QUIERE PARA CALCULAR EL AREA Y LA CIRCUNFERENCIA DE UN CIERCULO: "))

_area_of_circle_ = radio**2 * 3.14159
print(_area_of_circle_, "m2")
_circum_of_circle_ = 2*3.14159 * radio
print(_circum_of_circle_, "m")