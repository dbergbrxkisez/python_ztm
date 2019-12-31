# @decorators supercharge our function
# by adding some sort of decorators we supercharge our functions.


def hello(func):
    func()


def greet():
    print('still here!')


a = hello(greet)

print(a)


# Higher Order Function HOC
# map() reduce() filter() are all HOC
# It could either be a function that accepts another function inside of it's param or a function that returns another function.
def greet2(func):
    func()


def greet3():
    def func():
        return 5
    return func
