import sys

"""
if len (sys.argv) < 2:
    print("Too few arguments")
elif len (sys.argv) > 2:
    print("Too much arguments")
else:
    print("Hello, my name is", sys.argv[1])
    """
    
if len (sys.argv) < 2:
    sys.exit("Too few arguments")
    
#Slices, se partio la lista
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)