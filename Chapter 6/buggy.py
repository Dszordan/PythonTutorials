#buggy.py Bugs!
import random

number1 = random.randint(1,10)
number2 = random.randint(1,10)

print('what is ' + str(number1) + ' + ' + str(number2) + '?')

answer = input()

if answer == number1 + number2:
    print('correct')
else:
    print('nope!')
