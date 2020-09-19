import sys


def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1


user_input = input("Please input a number: ")
try:
    user_input = int(user_input)
except ValueError:
    print('Error Type, The game done.')
    sys.exit(0)

i = 1
while user_input != 1:
    print('The %d time, the number is %s.' % (i, user_input))
    user_input = collatz(user_input)
    i += 1
