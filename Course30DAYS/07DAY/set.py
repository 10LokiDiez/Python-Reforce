#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/Spanish/07_sets_sp.md

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

print(fruits)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

print(st3)

# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}

print(st1.intersection(st2))
print(st1.difference(st2))
print(st2.symmetric_difference(st1))