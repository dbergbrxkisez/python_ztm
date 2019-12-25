# Scope - what variable do I have access to?


total = 0


def count(total):
    total += 1
    return total


print(count(count(count(total))))
# 1 - start with local
# 2 - Parent local?
# 3 - Global
# 4 - built in python functions.
