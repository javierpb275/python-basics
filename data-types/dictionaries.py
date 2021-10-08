# Dictionary
# dict
dictionary = {
    'a': [1, 2, 3],
    'b': True,
    'c': 'hello',
    'd': 37
}

print(dictionary['a'][1])  # 2
print(dictionary)  # {'a': [1, 2, 3], 'b': True, 'c': 'hello', 'd': 37}

list_of_dictionaries = [
    {
        'a': [1, 2, 3],
        'b': True,
        'c': 'hello',
        'd': 37
    },
    {
        'a': [4, 5, 6],
        'b': False,
        'c': 'pepe',
        'd': 40
    }
]

print(list_of_dictionaries[1]['a'][2])  # 6
