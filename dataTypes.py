# data types:

# NUMBERS:
# int
my_integer = 1
# float
my_float = 2.5

# str
""" first_name = 'pepe'
last_name = 'lopez'
long_string = '''
This is
a long
string
------
'''
# string concatenation
full_name = first_name + ' ' + last_name

print(full_name)

# you cannot do: first_name + 5

# Type Conversion
print(type(int(str(100))))

# Escape Sequence
weather = "It's sunny"
weather2 = 'Its "kinf of" sunny'
weather3 = 'It\'s sunny'
weather4 = "It's \"kind of\" sunny"
weather5 = "\t It's \"kind of\" sunny\n have a nice day"
print(weather3)
print(weather4)
print(weather5) """

# formatted strings
name = 'pepe'
age = 30
print(f'Hi, my name is {name} and I\'m {age} ')
print('Hi, my name is {1} and I\'m {0} '.format(name, age))
print('Hi, my name is {new_name} and I\'m {new_age} '.format(new_name='paco', new_age=25))

""" 
bool
list
tuple
set
dict """

# Classes -> custom types

# Specialized Data Types: Special packages and modules that we can use from libraries.

# none: nothing. absence of value.
