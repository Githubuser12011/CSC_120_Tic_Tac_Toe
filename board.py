board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]

piecetype = " Pick your piece: "
rowmess = " select your row: "
colmess = " select your column: "

player1piece = None
player2piece = None

inputStack = []

isGameRunning = True

def checkDuplicates(player, row, col):
    invalidInput = False
    inputStack.append([row, col])
    if len(inputStack) == 2:
        if (inputStack[0] == inputStack[1]):
            invalidInput = True
            inputStack.pop()
        else:
            invalidInput = False

    if invalidInput:
        print("Invalid input. Duplicate entry.")
        handlePlayer(player)

def handlePlayerInput(player):
    invalidInput = False

    row = int(input(player + rowmess))

    if row < 0 or row > 2:
        invalidInput = True

    while invalidInput:
        print("Invalid input.")
        row = int(input(player + rowmess))
        if not row < 0 or not row > 2:
            invalidInput = False 
    
    col = int(input(player + colmess))

    if col < 0 or col > 2:
        invalidInput = True

    while invalidInput:
        print("Invalid input.")
        col = int(input(player + colmess))
        if not col < 0 or not col > 2:
            invalidInput = False

    checkDuplicates(player, row,col)
    
    return row, col


def handlePlayer(player):
    if player == "player1":
        player1piece = str(input(player + piecetype))
        row, col = handlePlayerInput(player)
        
        board[row][col] = player1piece
    elif player == "player2":
        player2piece = str(input(player + piecetype))
        row, col = handlePlayerInput(player)
        
        board[row][col] = player2piece        
    else:
        print("Invalid player")

def checkTheRows():
    board = [
    ['x', 'o', 'o'],
    ['x', 'o', 'o'],
    ['x', 'o', 'o'],
]
    column_check = {
        "left": [
            [0,0],
            [1,0],
            [2,0]
        ],

        "middle": [
            [0, 1],
            [1, 1],
            [2, 1],
        ],

        "right": [
            [0, 2],
            [1, 2],
            [2, 2],
        ]
    }

    diagonal_check = {
        "leftBottom": [ 
            [2,0],
            [1,1],
            [0,2]
        ],

        "rightBottom": [ 
            [0,0],
            [1,1],
            [2,2]
        ]
    },

    row_check = {
        "top": [
            [0,0],
            [0,1],
            [0,2]
        ],
        "middle": [
            [1,0],
            [1,1],
            [1,2]
        ],
        "bottom": [
            [2,0],
            [2,1],
            [2,2]
        ],
    }

    isWinner = False


    answer = []
    for index in range(len(board)):
        for other_index in range(len(board)):
            answer.append(board[other_index][index])
            if answer == column_check["left"] or answer == column_check["middle"] or answer == column_check["right"]:
                print(answer)

    print(isWinner)

checkTheRows()

isGameRunning = False
while isGameRunning:
    handlePlayer("player1")
    handlePlayer("player2")
    print(board)

 

