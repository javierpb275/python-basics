# str
first_name = 'pepe'
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
print(weather5)

# formatted strings
name = 'pepe'
age = 30
print(f'Hi, my name is {name} and I\'m {age} ')
print('Hi, my name is {1} and I\'m {0} '.format(name, age))
print('Hi, my name is {new_name} and I\'m {new_age} '.format(
    new_name='paco', new_age=25))

# string indexes
abc = 'abcdefghijklmnopqrstuvwxyz'
print(abc[0])  # a


# [start:stop:stepover] (string slicing)
the_numbers = '0123456789'
print(the_numbers[0:5])  # 01234
print(the_numbers[0:5:2])  # 024
print(the_numbers[5:])  # 56789
print(the_numbers[:5])  # 01234
print(the_numbers[::2])  # 02468
print(the_numbers[::-1])  # 9876543210


# immutability (strings cannot be changed. you cannot reasign PART of a string)
the_numbers = '0123456789'
#the_numbers[0] = '9'
the_numbers = '9'  # you have to create sth new
