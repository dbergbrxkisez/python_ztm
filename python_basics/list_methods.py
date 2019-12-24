basket = [1, 2, 3, 4, 5]

# ADDING


# just changing not updating
# new_list = basket.append(100)

# This updates the newly created list
# After we have appended then we can assign basket to new_list so that it points to basket which points to newly modified list

# basket.append(100)
#basket.insert(4, 100)

# new_list = basket
# print(basket)

basket.extend([100])

# print(new_list)


# REMOVING
#

# basket.pop()
# basket.pop(0)
# we give it the index
# basket.remove(4)
# we give it the value
new_list = basket.clear()
# clears th list completely
print(basket)
