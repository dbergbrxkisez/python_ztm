# Error Handling by wrapping all of my code in a try block
# It allows us to let the python script continue running even if there are errors
# Built in Exceptions: https://docs.python.org/3/library/exceptions.html

# we ask the user for an age and ask what is your age?

while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you')
        break
