# @decorators supercharge our function
# by adding some sort of decorators we supercharge our functions.


def hello(func):
    func()


def greet():
    print('still here!')


a = hello(greet)

print(a)
