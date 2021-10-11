# SET (unordered collections of unique objects)
# set
my_set = {1, 2, 3, 4, 5, 5}  # the last 5 never gets added
print(my_set)  # {1, 2, 3, 4, 5} (only returns the unique items from the set)

# in:
print(1 in my_set)  # True

# add():
my_set.add(2)
my_set.add(100)
print(my_set)  # {1, 2, 3, 4, 5, 100}

# set(): turn list into set
my_list = [6, 7, 8, 9, 9]
print(set(my_list))

# len():
print(len(my_set))

# list(): turn set into list
print(list(my_set))

# copy() and clear():
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)  # set()
