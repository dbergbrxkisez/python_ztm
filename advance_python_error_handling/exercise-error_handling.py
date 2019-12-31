# Error Handling
while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you')
        # break
    finally:
        print('ok, i\'m finally done')
    print('can you hear me?')

# finally runs regardless at the end of everything
# you wanna make sure the log of user login
