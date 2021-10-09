# dictionary methods
user = {
    'name': 'pepe',
    'age': 30
}

# get(): grab password from user, if it doesn't have that property, by default return 'secret'
print(user.get('password', 'secret'))
