# 20210624 Finishing Ch. 3 of ATBSWP with a collatz program

# Version A: Random Number
#import random
#num = random.randint(2,20)

# Version B: User input
print('Enter a starting number : ', end='')
while True:
    try:
        num = int(input())
        if num < 1:
            print('A number GREATER THAN 0....jackass. Try again.')
            print('')
            print('Enter a starting number : ', end='')
            continue
        break
    except ValueError:
        print('Idiot, enter a number. Try again.')
        print('')
        print('Enter a starting number : ', end='')
print('')
print('The starting number will be ' + str(num) + '.')
print('If even, then divide by 2.')
print('If odd, then multiply by 3 and add 1.')
print('Continue until 1.')
i = 1
while num != 1:
    print(str(i) + ': ' + str(num))
    if (num % 2) == 0: #number is even
        num = int(num / 2)
    else: #number is odd
        num = (num * 3) + 1
    i = i + 1
    
print(str(i) + ': ' + str(num))
print('Cool.')