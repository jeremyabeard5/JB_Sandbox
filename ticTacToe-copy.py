# 20210624 Using dictionaries to make a tic tac toe game

gameBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])
    
turn = 'X'
for i in range(9):
    printBoard(gameBoard)
    print(turn + ' turn. Move where? :', end='')
    move = input()
    gameBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
        
printBoard(gameBoard)
    
    