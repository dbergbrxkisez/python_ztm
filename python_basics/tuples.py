# Tuple
# A tuple is like list but unlike lists we cannot modify them
# They are immutable.
# benifits: don't need to change the list. and I want to stay as it is. code safer

my_tuple = (1, 2, 3, 4, 5, 5)
print(my_tuple[2])
print(5 in my_tuple)

new_tuple = my_tuple[1:2]
print(new_tuple)
new_tuple = my_tuple[1:4]
print(new_tuple)

print(my_tuple.count(5))
print("Index of tuple: " + str(my_tuple.index(5)))
print("Length of my_tuple: " + str(len(my_tuple)))

x, y, z, *other = (11, 12, 13, 14, 15)
print('x:' + str(x))
print(y)
print(z)
print('other: ' + str(other))

user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user.items())
print(user[(1, 2)])
