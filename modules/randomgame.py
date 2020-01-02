from random import randint
import sys

# generate a number 1-10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# input from user?
# check that input is a number 1~10
while True:
    try:
        print(answer)  # check the answer first
        guess = int(input(f'guess a number {int(sys.argv[1])}~{int(sys.argv[2])}:  '))
        if int(sys.argv[1]) < guess < int(sys.argv[2]):
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue

# check if number is the right guess. Otherwise
# ask again
