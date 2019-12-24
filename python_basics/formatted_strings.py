# formatted strings
# f before the string is known as formatted strings

name = 'Johhny'
age = 55

# string concatenation
print('hi ' + name + '. You are ' + str(age) + ' years old')

# formatted string
# make variables available inside a string
# python3 feature and highly recommended
print(f'hi {name}. You are {age} years old')

# not preffered used in python 2.
print('hi {new_name}. You are {age} years old'.format(
    new_name='sally', age=100))
