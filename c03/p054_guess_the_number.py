import random

secret_number = random.randint(1, 30)
print('I am thingking of a number between 1 and 30.')

for guess_taken in range(1, 100):
    print('Take a guess: ')
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        if guess == secret_number:
            print('Good job! You guessed number in %s guesses!' % guess_taken)
        else:
            print('Nope. The number I was thinking os was %s.' % secret_number)
        break
