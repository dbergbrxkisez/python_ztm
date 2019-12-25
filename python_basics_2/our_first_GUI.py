# clean
# Readability
# predictability
# DRY

# Exercise!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# 1. iterate over picture.
# if 0 -> print ''
# if 1 -> print *


fill = '*'
empty = ' '


def show_tree():
    for image in picture:
        for pixel in image:
            if (pixel):               # Truthy value either 0 or 1
                print(fill, end=" ")
            else:
                print(empty, end=" ")
        print('')  # need a new line after every image


show_tree()
show_tree()
show_tree()

print(show_tree)  # location of function in memory
