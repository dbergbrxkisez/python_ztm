# list, set, dictionary comprehension
# my_list = [param for param in iterable]
# my_list = [
#            expression(what we want to do with each item that we are iterating over)
#            loop(using a for loop through an iterable and give it a varibale which we gonna act upon)
#            if we want we also have an option to add a conditional and say only act upon this conditon based on True or False
# ]
# Hey Create A variable and then we are going to do a for loop saying hey for each variable in the iterable add it to the list.

# a list that contains a character in hello
my_list = [char for char in 'hello']
# a quick list with numbers ranging from 0 to 99
my_list2 = [num for num in range(0, 100)]
# a list where all the numbers are in multiplied by 2
my_list3 = [num*2 for num in range(0, 100)]
# my_list to the power of 2
my_list4 = [num**2 for num in range(0, 100)]
# Generate list of even numbers OR if num % 2 == 0 only then add to the list
my_list5 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list4)
