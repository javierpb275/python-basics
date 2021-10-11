# set methods
my_set_2 = {1, 2, 3, 4, 5}
my_set_3 = {4, 5, 6, 7, 8, 9, 10}

# difference():
difference_of_sets = my_set_2.difference(my_set_3)
print(difference_of_sets)  # {1, 2, 3}

# discard()
my_set_2.discard(5)
print(my_set_2)  # {1, 2, 3, 4}

# difference_update():
my_set_2.difference_update(my_set_3)
print(my_set_2)  # {1, 2, 3}

# intersection()
common_items = my_set_2.intersection(my_set_3)  # === my_set_2 & my_set_3
print(common_items)  # {4, 5}

# isdisjoint()
nothing_in_common = my_set_2.isdisjoint(my_set_3)
print(nothing_in_common)  # False (because of 4 and 5)

# union():
sets_together = my_set_2.union(my_set_3)  # === my_set_2 | my_set_3
print(sets_together)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# issubset() and issuperset()
my_set_4 = {4, 5}
my_set_5 = {4, 5, 6, 7, 8, 9, 10}

entire_set_is_inside_the_other_set = my_set_4.issubset(my_set_5)
print(entire_set_is_inside_the_other_set)  # True (because of {4,5})

set_contains_another_set = my_set_5.issuperset(my_set_4)
# True (because my_set_5 contains 4 and 5 plus other numbers)
print(set_contains_another_set)
