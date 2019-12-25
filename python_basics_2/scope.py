# Scope - what variable do I have access to?\
# Who has access to who?
if True:
    x = 10


def some_func():
    total = 100
    print(x)


a = 1


def confusion():
    a = 5
    return a


print(a)
print(confusion())
