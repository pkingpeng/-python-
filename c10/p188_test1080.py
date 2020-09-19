import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Tnter heads or tails:')
    guess = input()

toss = ('heads', 'tails')[random.randint(0, 1)]

if toss == guess:
    print('You got it!')
else:
    print('Nope, Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
