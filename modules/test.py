import random

print(random)
# help(random)
print(dir(random))  # All the methods on random
print(random.random())  # Any random nummber between 0 and 1
print(random.randint(1, 10))  # Random int between start and finish
print(random.choice([1, 2, 3, 4, 5]))

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
