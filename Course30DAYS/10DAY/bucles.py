person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key) # sólo imprime las claves

for key, value in person.items():
    print(key, value)
    
for number in range(11):
    print(number)
    
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)