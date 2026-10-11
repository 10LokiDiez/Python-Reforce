import sys

#python sys.py ...

#sys.argv sirve para ver las palabras que uso la persona antes de ejecutar el programa
#python 4sys.py Simon
#imprime Hello, my name is Simon
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("There is no name, too few arguments")
    
print("The program is:", sys.argv[0])