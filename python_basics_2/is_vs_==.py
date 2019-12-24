# == checks for equality in value
print('**** == ****')
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# checks where the location in memory is same where it is stored
print('**** is ****')
print(True is True)
print(True is 1)
print(1 is 1)
print([] is [])
print(10 is 10)
print('' is 1)
print([] is 1)
print(10 is 10.0)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a == b)
