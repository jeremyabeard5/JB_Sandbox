#! /usr/bin/python3
# 20210624 Implements a simple guessing game
import random
masterNum = random.randint(1,30)
print('I am thinking of a number between 1 and 30')
print('You get 5 guesses. Go.')

for numGuess in range(1,6):
    print('Try #: ' + str(numGuess))
    currentGuess = int(input())
    if currentGuess > masterNum:
        print('Your guess is too high.')
    elif currentGuess < masterNum:
        print('Your guess is too low.')
    else:
        break

if currentGuess == masterNum:
    print('You got it! My number was ' + str(masterNum) + '.')
else:
    print('Sorry, you lost. My number was ' + str(masterNum) + '.')
    
    
    
