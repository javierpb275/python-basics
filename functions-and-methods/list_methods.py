# built-in function:

basket = [1, 2, 3, 4, 5]
# len(): length
print(len(basket))

# list methods:

# adding

# append(): Append object to the end of the list.
append_list = [1, 2, 3, 4, 5]
append_list.append(6)
print(append_list)  # [1, 2, 3, 4, 5, 6]

# insert(): Insert object before index.
insert_list = [7, 8, 9, 10]
insert_list.insert(2, 36)
print(insert_list)  # [7, 8, 36, 9, 10]

# extend(): Extend list by appending elements from the iterable.
extend_list = [11, 12, 13, 14, 15]
extend_list.extend([16, 17, 18])
print(extend_list)  # [11, 12, 13, 14, 15, 16, 17, 18]

# removing
removeable_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# pop(): Remove and return item at index (default last).
# IMPORTANT: pop() returns whatever you've just removed
pop_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pop_list.pop()
print(pop_list)  # [1, 2, 3, 4, 5, 6, 7, 8]
pop_list.pop(0)
print(pop_list)  # [2, 3, 4, 5, 6, 7, 8]

# remove(): Remove first occurrence of value.
remove_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_list.remove(5)
print(remove_list)  # [1, 2, 3, 4, 6, 7, 8, 9]

# clear():Remove all items from list.
clear_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
clear_list.clear()
print(clear_list)  # []

# index():Return first index of value (__value: str, __start: SupportsIndex = ..., __stop: SupportsIndex = ...)
index_list = ['a', 'b', 'c']
print(index_list.index('b', 0, 2))  # 1

#count():Return number of occurrences of value.
count_list = [1,2,3,1]
print(count_list.count(1))#2

#keywords: in
print('c' in index_list)#True
print('i' in 'hi my name is pepe')#True