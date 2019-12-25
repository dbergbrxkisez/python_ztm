# Scope - what variable do I have access to?\
# Who has access to who?
#

if True:
    x = 10


def some_func():
    total = 100
    print(x)


a = 1


def parent():
    def confusion():
        return sum
    return confusion()


print(parent())
print(a)


# 1 - start with local
# 2 - Parent local?
# 3 - Global
# 4 - built in python functions.
