# Dictionary
# A key needs to be immutable.
# cannot be changed or has to have unique
# A string is immutable but a list is mutable
dictionary = {
    '123': [1, 2, 3],
    '123': 'hello'
}

print(dictionary['123'])
