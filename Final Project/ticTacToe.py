from random import randrange

ticBoard = [['_' for i in range(3)] for c in range(3)]
num = 1



#print(ticBoard)

def displayBoard(board):
    space = 1
    for row in range(3):
        print('\n|', end="")
        for col in range(3):
            if ticBoard[row][col] != '_':
                print(f' {ticBoard[row][col]} |', end="")
            else:
                print(f' {space} |', end='')
            space += 1
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def enter_move(board):
    pass
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def freeFieldList(board):
    freeSquare = []
    for row in range(3):
        for col in range(3):
            if ticBoard[row][col] == '_':
                freeSquare.append((row, col))
    return freeSquare
    
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.



def victoryCheck(board, sign):
    pass
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    pass
    # The function draws the computer's move and updates the board.


displayBoard(ticBoard)
#freeFieldList(ticBoard)
print("Free Tiles\n")
print(freeFieldList(ticBoard))