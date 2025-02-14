from random import randrange

ticBoard = [['_' for i in range(3)] for c in range(3)]
num = 1
moves = 0

print(randrange(9) + 1)

#print(ticBoard)

def displayBoard(board):
    space = 1
    for row in range(3):
        print('\n|', end="")
        for col in range(3):
            if board[row][col] != '_':
                print(f' {board[row][col]} |', end="")
            else:
                print(f' {space} |', end='')
            space += 1
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def enter_move(board):
    free = freeFieldList(board)
    displayBoard(board)


    moves += 1
    pass
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

def freeFieldList(board):
    freeSquare = {}
    space = 1
    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                freeSquare.update({ space : (row, col)}) # Pode ser feito em lista, mas eu queria usar dicionário. (Can be done with a list, but I wanted to use a dictionary)
            space += 1
    return freeSquare
    
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

def victoryCheck(board, sign):
    win = False

    if board[0][0] and board[1][1] and board[2][2] == sign or board[0][2] and board [1][1] and board[2][0] == sign:
        win = True

    for lin in range(3):
        if board[lin][lin] and board[lin][lin + 1] and board[lin][lin + 2] == sign:
            win = True
        if board[lin][lin] and board[lin + 1][lin] and board[lin + 2][lin] == sign:
            win = True
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if win == True: print(f'Jogador {sign} Venceu!')
    else: print('O jogo Continua!')


def draw_move(board):
    if moves == 0: board[1][1] = 'X'


    moves += 1
    # The function draws the computer's move and updates the board.


displayBoard(ticBoard)
#freeFieldList(ticBoard)
print("\n\nFree Tiles\n")
print(freeFieldList(ticBoard))