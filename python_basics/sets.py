# set
# only returns the unique item
# no repated values
# not ordered as list like right next to each other. every item is randomly placed
# if already exists then not added again


my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set)
# print(my_set[0])     This is gives and error
# print(1 in my_set)
print(len(my_set))  # it gives 6 coz of set rule = no repated items in it
print(list(my_set))  # it gets converted to list with no repeat

# if we copy the set to a new one and clear the first one then new_set remains as it was assigned.
new_set = my_set.copy()
my_set.clear()
print(list(new_set))
print(my_set)

# a list returning only unique items
# collecting emails but no chance of duplicate emails.

my_list = [1, 2, 3, 4, 5, 5]

print(set(my_list))
