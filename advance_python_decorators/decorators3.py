# Decorator Pattern
# It gives our decorator flexibility so that we are able to pass as many argumnts as we want into a wrapped function by using *args and **kwargs and then unpacking them as this function.


def my_decorator(func):
    def wrap_function(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_function


# WHAT HAPPENS IF HELLO FUNCTION TAKES AN ARGUMENT?
@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


# hello('hiiiii', ':)')
hello('hiiiiii')
