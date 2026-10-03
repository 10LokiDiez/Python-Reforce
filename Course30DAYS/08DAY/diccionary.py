#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/Spanish/08_dictionaries_sp.md

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street

print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland

person['job_title'] = 'Instructor'
person['skills'].append('HTML')

values = person.values()
print(values)