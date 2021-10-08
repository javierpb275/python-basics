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


# dictionary keys (always have to be immutable)
my_dictionary = {
    123: [1, 2, 3],
    True: 'Pepe',
    'number': 82,
}

# a key always has to be unique (if we have two keys that are equal, the last one overwrtites the previous one)
my_dictionary_2 = {
    '123': [1, 2, 3],
    '123': 'Pepe',
    'number': 82,
}

print(my_dictionary_2['123'])  # Pepe
