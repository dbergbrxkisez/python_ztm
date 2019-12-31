# Decorator
# Decorators is a function, like my_decorator that wraps another function,
# which is the function that we pass it and enhances it.


def my_decorator(func):
    def wrap_function():
        print('**********')
        func()
        print('**********')
    return wrap_function

# by just using this @my_decorators we can extend functionalities.


@my_decorator
def hello():
    print('hellloooo')


@my_decorator
def bye():
    print('see ya later')


# wrapping hello function with my_decorator and assigning to a variable
# Step by Step
# hello2 = my_decorator(hello)
# hello2()

# my_decorator(hello)()

# hello()
# bye()
