basket = [1, 2, 3, 4, 5]

# ADDING

# just changing not updating
# new_list = basket.append(100)

# This updates the newly created list
# After we have appended then we can assign basket to new_list so that it points to basket which points to newly modified list
# basket.append(100)
# new_list = basket
# print(basket)

# print(new_list)

basket.extend([100])


# removing
new_list = basket.clear()
print(basket)
