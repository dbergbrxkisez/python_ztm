# lambda expressions | used for functions that are only need to use once. They are anonymous function
# lambda param: function(param)
# lambda param: manupulation(param)
# lambda param: action(param)
# after : it automatically returns
# more on lambda in comprehensions

from functools import reduce
my_list = [1, 2, 3]

# non longer need these functions if we use lambda

# def multiply_by2(item):
#     return item*2


# def only_odd(item):
#     return item % 2 != 0


# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item


# no name function used only for once
# one line functions

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list))

# print(my_list)
