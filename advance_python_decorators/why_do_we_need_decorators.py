# Decorator
# A performance decorator that I can use during testing my code.
# To see how fast my code runs

# built in module
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


while True:
    long_time()
