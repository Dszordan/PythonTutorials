# guess.py Guessing Game
import random

guessesTaken = 0
myName =''
randomNumber = 0

print('Hey there, what\'s your name?')
myName = input()

randomNumber = random.randint(1,20)
print('hey, ' + myName + ', I am thinking of a number between 1 and 20')

while guessesTaken < 6:
    print('take a guess')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < randomNumber:
        print('your guess is too low.')

    if guess > randomNumber:
        print('your guess is too high.')

    if guess == randomNumber:
        break

if guess == randomNumber:
    guessesTaken = str(guessesTaken)
    print ('Good job. You guessed the number in ' + guessesTaken + ' guesses!')

if guess != randomNumber:
    number = str(randomNumber)
    print('Nope, you failed.')
