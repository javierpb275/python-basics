# TUPLE (imutable lists)
# tuple
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[4])  # 5
print(5 in my_tuple)  # True

new_tuple = my_tuple[1:2]
print(new_tuple)  # (2,)

x, y, z, *others = (1, 2, 3, 4, 5)
print(y)  # 2
print(others)  # [4, 5]

#tuple methods:
print(my_tuple.count(5))#1
print(my_tuple.index(5))#4

#built-in function
print(len(my_tuple))#5