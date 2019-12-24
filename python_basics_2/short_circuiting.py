# Short Circuiting

is_Friend = True
is_User = True

if (is_Friend and is_User):
    print('and best-friends forever')


# short cicuiting
# more performant
if (is_Friend or is_User):
    print('or best-friends forever')
