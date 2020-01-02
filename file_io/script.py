# https://docs.python.org/3/library/pathlib.html
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
#
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
#
# a list that contains entire file and reads all the lines.
# print(my_file.readlines())
# my_file.close()
#
#
# read | This is a standard way to read the file.
with open('app/sad.txt', mode='r') as my_file:
    print(my_file.read())

# write | overrides the existing or creates new file.
# with open('test.txt', mode='w') as my_file:
#     text = my_file.write(':)')
#     print(my_file.readlines())
# with open('app/sad.txt', mode='w') as my_file:
#     text = my_file.write(':(')
#     print(my_file.readlines())

# read and write
# with open('test.txt', mode='r+') as my_file:
#     text = my_file.write(':)')
#     print(text)

# append | appends to the end of the file.
# with open('test.txt', mode='a') as my_file:
#     text = my_file.write(':)')
#     print(text)
