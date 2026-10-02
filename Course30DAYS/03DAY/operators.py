#Aqui podemos ver los operadores de Asignacion y hay otros:
#https://www.w3schools.com/python/python_operators_assign.asp

edad = 20
altura = 1.71
complej = 7j -1

base = int(input("Entada base: "))
altura2 = int(input("Entada altura: "))
print(f"El área del triángulo es {(base//2) *altura2 }")
print(3 > 2)     # True, porque 3 es mayor que 2
print(3 >= 2)    # True, porque 3 es mayor que 2
print(3 < 2)     # False,  porque 3 es mayor que 2
print(2 < 3)     # True, porque 2 es menor que 3
print(2 <= 3)    # True, porque 2 es menor que 3
print(3 == 2)    # False, porque 3 no es igual a 2
print(3 != 2)    # True, porque 3 no es igual a 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparación booleana
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Comparación de otra forma
print('1 is 1', 1 is 1)                   # True - porque los valores de los datos son los mismos
print('1 is not 2', 1 is not 2)           # True - porque 1 no es 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A encontrado en la cadena
print('B in Asabeneh', 'B' in 'Asabeneh') # False - no hay b mayúscula
print('coding' in 'coding for all') # True - porque codificar para todos tiene la palabra codificar
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - porque ambas afirmaciones son verdaderas
print(3 > 2 and 4 < 3) # False - porque la segunda afirmación es falsa
print(3 < 2 and 4 < 3) # False - porque ambas afirmaciones son falsas
print(3 > 2 or 4 > 3)  # True - porque ambas afirmaciones son verdaderas
print(3 > 2 or 4 < 3)  # True - porque uno de los enunciados es verdadero
print(3 < 2 or 4 < 3)  # False - porque ambas afirmaciones son falsas
print(not 3 > 2)     # False - porque 3 > 2 es verdadero, entonces not verdadero da falso
print(not True)      # False - Negación, el operador not devuelve verdadero a falso
print(not False)     # True
print(not not True)  # True
print(not not False) # False