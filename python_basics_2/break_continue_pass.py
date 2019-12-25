# break - breaks out of the current and closing
# continue - whatever happens when you hit this line, continue onto the top of the closing loop
# pass - It just passes to the next line,
#      - Placeholder while coding

my_list = [1, 2, 3]
for item in my_list:
    continue
    print(item)

for item in my_list:
    # thinking about it
    print('now pass will be interpreted.')
    pass


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    print('noww loop breaks')
    break
