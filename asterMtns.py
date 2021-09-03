#! /usr/bin/python3
# 20210902 snaking asterisk mountains visualization project
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
PAUSETIME = 0.03 # standard = 0.03, less for faster, greater for slower


# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1
WIDTH -= 4 # accouting for the 4 characters of showing position

position = 1 #initialize

# write function to create a 3-digit string of the current position
# essentially, just adds leading zeros
def formStr(position):
    if len(str(position)) == 1:
        return '00'+str(position)+' '
    elif len(str(position)) == 2:
        return '0'+str(position)+' '
    else:
        return str(position)+' '

# calculates an appropriate random amount to move forward (right) by
def moveForward(position, printStr):
    randomForward = random.randint(1, WIDTH-position-1)
    for i in range(randomForward):
        print(formStr(position) + printStr)
        time.sleep(PAUSETIME)
        printStr += '*'
        position += 1
    return [position, printStr]
    
# calculates an appropriate random amount to move backward (left) by        
def moveBackward(position, printStr):
    randomBackward = random.randint(1, position-1)
    for i in range(randomBackward):
        print(formStr(position) + printStr)
        time.sleep(PAUSETIME)
        printStr = printStr[:-1]
        position -= 1
    return [position, printStr]

def exitSequence():
    print()
    print('Asterisk Mountains, by Jeremy Beard ' + chr(9787))
    sys.exit()

# print screen width for initialization / debugging / verification purposes
print()
print('Asterisk Mountains, by Jeremy Beard ' + chr(9787))
print('Screen Width = ', WIDTH)
time.sleep(1) # pause

# initialization sequence is just a straight increase from 1 to the screenwidth
print('Initializing.', end='')
for i in range(8):
    time.sleep(0.5)
    print('.', end = '')
time.sleep(0.5)
print('.')
time.sleep(0.5)

initStr = '*'
for i in range(WIDTH):
    print(formStr(position) + initStr)
    position += 1
    initStr += '*'    
    time.sleep(0.01)
print()
print()
time.sleep(1)

# begin random sequence
position = 1
positionModifier = -1
printStr = '*'
while True: # infinite loop of pleasant randomness
    try:
        [position, printStr] = moveForward(position, printStr)
        [position, printStr] = moveBackward(position, printStr)
    except KeyboardInterrupt:
        exitSequence()
    
    
# if this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exitSequence()
    
