# list, set, dictionary comprehension

# SET COMPREHENSION
# a set that contains a character in hello
my_set = {char for char in 'hello'}
# a quick set with numbers ranging from 0 to 99
my_set2 = {num for num in range(0, 100)}
# a set where all the numbers are in multiplied by 2
my_set3 = {num*2 for num in range(0, 100)}
# my_set to the power of 2
my_set4 = {num**2 for num in range(0, 100)}
# Generate set of even numbers OR if num % 2 == 0 only then add to the set
my_set5 = {num**2 for num in range(0, 100) if num % 2 == 0}

# print(my_set4)

# DICTIONARY COMPREHENSION
# dictionary with a key value pair and the value gets acted upon
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items()
           if value % 2 == 0}

my_dict2 = {num: num**2 for num in [1, 2, 3]}
print(my_dict2)
