# parameters | used on defining the function
# Default Parameters | assigns a default value if not defined


def say_hello(name='Darth Vader', emoji='😈'):
    print(f'helllloooooooo {name}{emoji}')


# arguments | used when we call/invoke the function
# positional arguments | are arguments that require to be in proper position
say_hello('D', '😋')
say_hello('Dan', '😋')
say_hello('Emily', '😋')

# keyword arguments | this is bad practice
say_hello(emoji='😋', name='Bibi')
say_hello()
say_hello('Timmy')
