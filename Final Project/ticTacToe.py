from random import randrange

ticBoard = [['_' for i in range(3)] for c in range(3)]
num = 1
moves = 0

#print()

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
    freeFieldList(board)
    valid = False
    global moves 

    while not valid:
        displayBoard(board)
        play = int(input('\nSelecione o local que deseja jogar. >'))
        if play > len(free) or play < 1:
            print("Movimento Invalido. Invalid Movement")
        else:
            r, c = free[play - 1]
            board[r][c] = "O"           
            valid = True
        
    
    moves += 1 
    victoryCheck(board, "O")
        

    # moves += 1
    
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

def freeFieldList(board): # Tornarei em um dicionário futuramente para ver se é possivel. (Will turn into a dictionary in the future to see if it's possible.)
    freeSquare = []
    #space = 0 Seria usado como chave do dicionário (Would be used as the dictionary's Key.)
    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                freeSquare.append((row, col))
    return freeSquare
    
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

def victoryCheck(board, sign):
    win = False
    status = freeFieldList(board)

    
    


    if board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign:
        win = True

    for lin in range(3):
        if board[lin][0] == board[lin][1] == board[lin][2] == sign:
            win = True
        if board[0][lin] == board[1][lin] == board[2][lin] == sign:
            win = True
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if win == True: 
        displayBoard(board)
        print(f'\nJogador {sign} Venceu!')
    else: 
        if not status:
            displayBoard(board)
            print('\nEmpate!')
            return
        if sign == "O":
            draw_move(board)
        else: enter_move(board)

    


def draw_move(board):
    global moves 

    if moves == 0: board[1][1] = 'X'
    else: 
        free = freeFieldList(board)
        row, col = free[randrange(len(free))]
        board[row][col] = "X"
    moves += 1

    victoryCheck(board, "X")
    # The function draws the computer's move and updates the board.
    #First move is always in the middle (Position 1, 1)


draw_move(ticBoard)