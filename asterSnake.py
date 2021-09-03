#! /usr/bin/python3
# 20210902 snaking asterisk visualization project
# Author: Jeremy Beard
# Source: childhood

import sys, random, time

try:
    import bext # using bext to get screen dimensions
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()
        
# Set up the constants:
WIDTH, HEIGHT = bext.size() # screensize
PAUSETIME = 0.05 # standard = 0.03, less for faster, greater for slower

# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1
WIDTH -= 2 # accounting for edges

def exitSequence():
    print()
    print('Asterisk Mountains, by Jeremy Beard ' + chr(9787))
    sys.exit()

def getSnakes():
    while True:
        print()
        print('How many snakes to create?')
        snakesInput = input('> ')
        if snakesInput.isdecimal():
            snakesInput = int(snakesInput.strip())
        else:
            print('INPUT ERROR: Please enter integer between 1 and 100')
        
        if snakesInput > 0 and snakesInput < 101:
            return snakesInput
        else:
            print('INPUT ERROR: Please enter integer between 1 and 100')

def move(snk):
    # we've got snk[DIR] ('RIGHT' or 'LEFT')
    #           snk[POSITION] (integer 1 to WIDTH)
    #           snk[FINAl_POS] (integer 1 to width)
    #           snk[SNAKE_STR] ('*')

    if snk[POSITION] == 1 and snk[DIR] == LEFT:
        if snk[POSITION] == snk[FINAL_POS]:
            snk[FINAL_POS] = snk[POSITION] + random.randint(1, WIDTH - snk[POSITION])
        snk[DIR] = RIGHT
    elif snk[POSITION] == WIDTH and snk[DIR] == RIGHT:
        if snk[POSITION] == snk[FINAL_POS]:
            snk[FINAL_POS] = snk[POSITION] - random.randint(1, snk[POSITION] - 1)
        snk[DIR] = LEFT
    elif snk[POSITION] == 1 and snk[DIR] == RIGHT:
        if snk[POSITION] == snk[FINAL_POS]:
            snk[FINAL_POS] = snk[POSITION] + random.randint(1, WIDTH - snk[POSITION])
    elif snk[POSITION] == WIDTH and snk[DIR] == LEFT:
        if snk[POSITION] == snk[FINAL_POS]:
            snk[FINAL_POS] = snk[POSITION] - random.randint(1, snk[POSITION] - 1)         
    elif snk[POSITION] == snk[FINAL_POS]:
        if snk[DIR] == LEFT:
            snk[DIR] = RIGHT
            snk[FINAL_POS] = snk[POSITION] + random.randint(1, WIDTH - snk[POSITION])
        elif snk[DIR] == RIGHT:
            snk[DIR] = LEFT
            snk[FINAL_POS] = snk[POSITION] - random.randint(1, snk[POSITION] - 1)
               
    if snk[DIR] == RIGHT:
        snk[POSITION] += 1
    elif snk[DIR] == LEFT:
        snk[POSITION] -= 1

def buildStr(snakes):
    returnStr = ' '
    returnStr *= (WIDTH + 2) # add 2 for the border characters '|'
    returnStr = list(returnStr)
    for i, char in enumerate(returnStr):
        positionHere = False
        for snake in snakes:
            if snake[POSITION] == i:
                positionHere = True
        if positionHere:
            returnStr[i] = '*'
            
    returnStr[0] = '|'
    returnStr[-1] = '|'
    return returnStr        
    

# print screen width for initialization / debugging / verification purposes
print()
print('Asterisk Mountains, by Jeremy Beard ' + chr(9787))
print('Screen Width = ', WIDTH)
time.sleep(1) # pause

NUM_SNAKES = getSnakes()
RIGHT = 'r'
LEFT = 'l'
DIRECTIONS  = (RIGHT, LEFT)

POSITION = 'position'
DIR = 'dir'
FINAL_POS = 'final_pos'
SNAKE_STR = 'snake_str'
snakes = []
for i in range(NUM_SNAKES):
    snakes.append({POSITION: random.randint(1, WIDTH),
                   DIR: random.choice(DIRECTIONS),
                   FINAL_POS: 0,
                   SNAKE_STR: '*'})
    snakes[-1][FINAL_POS] = snakes[-1][POSITION]
    if snakes[-1][POSITION] == 1 and snakes[-1][DIR] == LEFT:
        snakes[-1][DIR] = RIGHT
    if snakes[-1][POSITION] == WIDTH and snakes[-1][DIR] == RIGHT:
        snakes[-1][DIR] = LEFT
    
    

# initialization sequence is just a straight increase from 1 to the screenwidth
print('Initializing.', end='')
for i in range(8):
    time.sleep(0.5)
    print('.', end = '')
time.sleep(0.5)
print('.')
time.sleep(0.5)

initStr = '*'
position = 1 #initialize
for i in range(WIDTH+2):
    print(initStr) # former version of code is : print(formStr(position) + initStr)
    position += 1
    initStr = ' ' + initStr # this line of code was changed from asterMtns.py    
    time.sleep(0.01)
print()
print()
time.sleep(1)
# end initialization sequence
    

# begin sequence
while True: # infinite loop of pleasant randomness
    try:
        for snake in snakes:
            snake = move(snake)
        line = buildStr(snakes)
        print("".join(line))
        time.sleep(PAUSETIME)
    except KeyboardInterrupt:
        exitSequence()
    
    
# if this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exitSequence()
    
