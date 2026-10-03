#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/Spanish/04_strings_sp.md
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # nueva línea
print('Days\tTopics\tExercises') # añade una tabulación
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')

print('This is a backslash  symbol \\) \" \{\}')

language = 'Python'

first_letter = language[0]
print(first_letter) # P

second_letter = language[1]
print(second_letter) # y

last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n


first_three = language[0:3] # empieza en índice 0, hasta 3 pero sin incluir 3
print(first_three) #Pyt

greeting = 'Hello, World!'
print(greeting[::-1])

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, cuenta entre índices 7 y 14
print(challenge.count('th')) # 2

print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

sub_string = 'yt'
print(challenge.index(sub_string))  # 7

print("python for everyone".replace("everyone", "all"))

cadena = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'

print(cadena.replace(" ", "").split(","))