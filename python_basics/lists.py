# List is an orderd sequence of objects. That can be of any type.
# inside of [] we can have different objects
# In python lists are a form of array.(like arrays but not array's to be specific)
# next to each other

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# Data Structure
# It's a way for us to organize information and data into let's say a folder, cupboard, box. etc.
# A container around your data that different pros and cons of accessing, removing, updating data.


amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart[0])
print(amazon_cart[1])
# nothin exists... cannot be accessed.
# print(amazon_cart[2])


# List Slicing
print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]      # : copies and == will point to the same
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
