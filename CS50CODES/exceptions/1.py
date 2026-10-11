#Aqui erroja un errror SyntaxError
# print("Hello, world)
#Tienen que ser solucionados
def main():
    x = get_int()
    print(f"x is {x}")
    
#ValueError, error de valor
def get_int():
    while True:
        try:
            x = int(input("Whats x? "))
        except ValueError:
            #pass para que simplemente lo coja y haga su funcion
            print("x is not an integer")
        #Se ejecuta SOLO si es un success
        else:
            return x
      
#NameError, error si esa variable no existe
main()