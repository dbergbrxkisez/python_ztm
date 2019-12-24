#  str = string
# int = integer

# converted 100 to str
print(type(str(100)))

# int to str to int and print
print(type(int(str(100))))


a = str(100)
b = float(a)
c = type(b)
print(c)
# Type Conversion


# Exercise
birth_year = input('what year were you born?')
age = 2019 - int(birth_year)

print(f'your age is: {age}')
