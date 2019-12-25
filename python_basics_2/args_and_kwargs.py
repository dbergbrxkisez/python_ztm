#  *args **kwargs(keyword args)


# This can accept any number of positional arguments like this
def super_func(name, *args, i='hi', **kwargs):
    total = 0
    print(args)   # gives a Tuple of arguments
    print(*args)
    print(kwargs)
    print(*kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func('Andy', 1, 2, 3, 4, 5, num1=5, num2=10))

# Rule of Ordering of Parameters:  params, *args, default parameters, **kwargs
# def super_func(name, *args, i='hi' ** kwargs):
