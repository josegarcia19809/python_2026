# Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.

'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''
from fontTools.merge.util import first


def extract_full_name(lista):
    nueva_lista = []
    for elemento in lista:
        nueva_lista.append(elemento['first'] + " " + elemento['last'])
    return nueva_lista


def extract_full_name2(lista):
    return list(map(lambda val: f"{val['first']} {val['last']}", lista))


names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

print(extract_full_name(names))
