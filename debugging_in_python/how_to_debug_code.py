# debugging
# https://docs.python.org/3/library/pdb.html

# linting
# ide / editor
# read errors(15-20 errors 90% of time)
# pdb(built in module) python debugger for py interpreter

import pdb

def add(num1, num2):
    # print(num1,num2)
    pdb.set_trace()  # Awesome to step through the code.
    t = 4 * 5
    return num1+num2

add(4, 5)


