# 20210624: Testing the sys.exit() function
import sys
while True:
    print('Type exit to exit:')
    response = input()
    if response == 'exit':
        print('Exiting...')
        sys.exit()
    print('Not exiting because you typed: ' + response + '.')