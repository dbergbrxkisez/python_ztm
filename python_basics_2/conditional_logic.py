is_old = bool('Hello')
is_licenced = bool(5)


# if is_old and is_licenced:
#     print('you are old enough to drive, and you have a licence!')
# # elif condition:
# # elif condition:
# else:
#     print('you are not of age!')
#     print('okoko')


print(bool('hello'))
print(bool(''))
print(bool(5))
print(bool(0))
print(bool(None))
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

# Truthy and Falsy

password = '123'
username = 'Johnny'

if password and username:
    print('you are old enough to drive, and you have a licence!')
else:
    print('you are not of age!')
    print('okoko')
