# set
# only returns the unique item
# no repated values
# not ordered as list like right next to each other. every item is randomly placed
# if already exists then not added again


my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)
# print(my_set)
# print(my_set[0])     This is gives and error
# print(1 in my_set)
# print(len(my_set))  # it gives 6 coz of set rule = no repated items in it
# print(list(my_set))  # it gets converted to list with no repeat

# if we copy the set to a new one and clear the first one then new_set remains as it was assigned.
new_set = my_set.copy()
my_set.clear()
# print(list(new_set))
# print(my_set)

# a list returning only unique items
# Example: collecting emails but no chance of duplicate emails.

# my_list = [1, 2, 3, 4, 5, 5]

# print(set(my_list))


# Methods on sets.
print('Methods on Sets:  ')

my_set_methods = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

#  .difference()
# print(my_set_methods.difference(your_set))    # This just tells the difference

# #  .discard()
# print(my_set_methods.discard(5))
# print(my_set_methods)             # modified discarded set

#  .difference_update()
# This updates the difference/ modifies the difference
# print(my_set_methods.difference_update(your_set))
# print(my_set_methods)

#  .intersection()
# both produces the same result
# print(my_set_methods.intersection(your_set))
# print(my_set_methods & your_set)

#  .isdisjoint()
# are they overlapping| have in common True if nothing in common
# print(my_set_methods.isdisjoint(your_set))

#  .issubset()
print(my_set.issubset(your_set))

#  .issuperset()
print(my_set_methods.issuperset(your_set))
print(your_set.issuperset(my_set_methods))

#  .union()
# both produces the same result
# print(my_set_methods.union(your_set))
# print(my_set_methods | your_set)
