# LIST
# list
li_1 = [1, 2, 3, 4, 5]
li_2 = ['a', 'b', 'c']
li_3 = [1, 2.5, 'a', True]

print(li_3[1])  # 2.5

# Data Structure: the way to organize information or data. a container arround your data that has different pros and cons of accessing that data

# List slicing: [start:stop:stepover]
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart[0:2])  # ['notebooks','sunglases']
print(amazon_cart[0::2])  # ['notebooks','toys']

# lists are mutable:
amazon_cart[0] = 'books'
new_cart = amazon_cart[0:3]  # with list slicing we are creating a new list
new_cart[0] = 'laptop'
print(new_cart)  # ['laptop', 'sunglasses', 'toys']
print(amazon_cart)  # ['books', 'sunglasses', 'toys', 'grapes']

# we are saying: the value of fruits_2 is whatever the value of fruits is
fruits = ['orange', 'apple', 'banana', 'strawberry', 'watermelon']
fruits_2 = fruits  # <- modify
fruits_2[0] = 'grape'
print(fruits_2)  # ['grape', 'apple', 'banana', 'strawberry', 'watermelon']
print(fruits)  # ['grape', 'apple', 'banana', 'strawberry', 'watermelon']

# if you wanna copy a list, you do this:
fruits_2 = fruits[:]  # <- copy
fruits_2[0] = 'pineapple'
print(fruits_2)  # ['pineapple', 'apple', 'banana', 'strawberry', 'watermelon']
print(fruits)  # ['grape', 'apple', 'banana', 'strawberry', 'watermelon']

# Matrix
matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
print(matrix[0][1])  # 0

# common list patterns
my_list = ['a', 1, 'b', 2, 'c', 3]
print(len(my_list))  # 6
print(my_list[::-1])  # [3, 'c', 2, 'b', 1, 'a']
print(my_list[:])  # ['a', 1, 'b', 2, 'c', 3]
print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(11)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sentence = '!'
new_sentence = sentence.join(['hi', 'i', 'am', 'pepe'])
print(new_sentence)  # hi!i!am!pepe
sentence_2 = ' '.join(['hi', 'i', 'am', 'pepe'])
print(sentence_2)  # hi i am pepe

# list unpacking
a, b, c, *others, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a, b, c)  # 1 2 3
print(others)  # [4, 5, 6, 7, 8]
print(d)  # 9
