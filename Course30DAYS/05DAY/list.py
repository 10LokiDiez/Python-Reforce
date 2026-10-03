#https://docs.python.org/es/3/tutorial/datastructures.html
#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/Spanish/05_lists_sp.md
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
full_stack.extend(["Python","SQL"])
print(full_stack)

fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
#MUY IMPORTANTE
print(rest)           # ['lemon','lime','apple']


first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

orange_and_mango = fruits[1:3]

print(orange_and_mango)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(max(ages))
print(min(ages))