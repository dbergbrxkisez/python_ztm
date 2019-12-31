# somethime errors and exceptions can be so severe that we do want to stop programms from running
# If we want to show the error what we do instead of except block raise ValueError('hey cut it out)

while True:
    try:
        age = int(input('what is your age? '))
        10/age
        # It could be anything like we kept keyword 'exception'
        raise Exception('hey cut it out')
        # raise ValueError('hey cut it out')
    # except ValueError:
    #     print('Please enter a number')
    #     continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you')
        # break
    finally:
        print('ok, i\'m finally done')
    print('can you hear me?')


# Errors are unavoidable but we have to handle those errors
