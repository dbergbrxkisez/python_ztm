# A list is an iterable(something that we can iterate through) it has __iter__ method. So, when the object is created __iter__ allows to have iterable object that can be iterated over.
# Iteration is the act of taking an item from an iterable, doing something to it. Then move to the next one. When we use loops(for, while loops) we call that iteration. It's the process itself.
# Generators are actually iterable that is a generator is iterable. You can iterate over them.
# But not everything that iterable is a generator

# iterable
# iterate
# generators

# for ex. range is a generator and is always going to be iterable
# But an list is iterable but is not a generator.
# range(100)

# SO A GENERATOR IS A SUBSET OF ITERABLE


def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(100)
next(g)
next(g)
print(next(g))
print(next(g))

# for item in generator_function(1000):
#     print(item)


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result


# my_list = make_list(100)
# print(my_list)
# print(list(range(1000000)))
