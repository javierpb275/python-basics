# BUILT-IN FUNCTIONS:

#grabs the value typed in the terminal and store it in the variable asigned:
name = input("what's your name? ")
#print message in the terminal:
print("Hello " + name)

# len(): length
print(len('012345'))  # 6
name = 'javier'
print(name[0:len(name)])  # javier


# METHODS:

quote = 'to be or not to be'

# upper(): uppercase
print(quote.upper())

# lower(): lowercase
print(quote.lower())

# capitalize(): capitalize the beginnig of the sentence
print(quote.capitalize())

# find(): it tells the index of the first 'be
print(quote.find('be'))  # 3
print(quote.find('m'))  # -1

# replace():
print(quote.replace('be', 'me'))

print(quote)  # to be or not to be. Strings are immutable. We can overwrite them. We either create them or destroy them
