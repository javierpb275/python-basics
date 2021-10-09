# dictionary methods
user = {
    'name': 'pepe',
    'age': 30
}

# get(): grab password from user, if it doesn't have that property, by default return 'secret'
print(user.get('password', 'secret'))


my_dictionary = {
    123: [1, 2, 3],
    True: 'Pepe',
    'number': 82,
    'Paco': False
}

user2 = dict(name='paco', age=34)

# keys():
print('number' in my_dictionary.keys())  # True
# values():
print(82 in my_dictionary.values())  # True
# items():
print(my_dictionary.items())# dict_items([(123, [1, 2, 3]), (True, 'Pepe'), ('number', 82), ('Paco', False)])


# copy():
user3 = user2.copy()
print(user3)
# clear():
user2.clear()
print(user2)  # {}



my_dictionary2 = {
    'name': 'dictionary 2',
    'number': 24,
    'isSth': False
}

# pop():
print(my_dictionary2.pop('isSth'))  # False
print(my_dictionary2)  # {'name': 'dictionary 2', 'number': 24}

# update():
print(my_dictionary2.update({'number': 25}))  # None
print(my_dictionary2)  # {'name': 'dictionary 2', 'number': 25}
print(my_dictionary2.update({'new_property': 'new_value'}))  # None
print(my_dictionary2)  # {'name': 'dictionary 2', 'number': 25, 'new_property': 'new_value'}

# popitem(): randomly pops off sth
print(my_dictionary2.popitem())  # ('number', 25)
print(my_dictionary2)  # {'name': 'dictionary 2'}
