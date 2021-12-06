# CSC 120 Tic Tac Toe Game
# Created by Bryan Rojas (brojas1200) and Paul Ruiz Wilson (Githubuser12011)
# Globals:
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]
isGameRunning = True

piecetype = " Pick your piece: "
rowmess = " Select your row: "
colmess = " Select your column: "

player1piece = None
player2piece = None

selectedPieces = {
    "player1": None,
    "player2": None
}

# Board logic:
def bindToBoard(functionToBind, playerToBind):
    bindedReturn = None
    for row in range(len(board)):
        for row_element in range(len(board)):
            bindedReturn = functionToBind(row, row_element, playerToBind)
    return bindedReturn
def printBoard(row, row_element):
    print(row, row_element)
def resetBoard(row, row_element):
    board[row][row_element] = '-'
def checkColumns(row, row_element, player):
    hasWon = True
    if board[row][row_element] != selectedPieces[player]:
        hasWon = False
    return hasWon
def checkRows(row, row_element, player):
    hasWon = True
    if board[row][row_element] != selectedPieces[player]:
        hasWon = False
    return hasWon
def checkDiagonal(row, row_element, player):
    hasWon = True
    if board[row][row] != selectedPieces[player]:
        hasWon = False
    return hasWon
def checkInverseDiagonal(row, row_element, player):
    hasWon = True
    if board[row][len(board) - row] != selectedPieces[player]:
        hasWon = False
    return hasWon
def checkFullBoard(row, row_element):
    if board[row][row_element] == '-':
        return False
    return True


# inputStack is a stack to make sure there are no duplicates.
inputStack = []


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
    if bindToBoard(checkColumns, player) or bindToBoard(checkRows, player) or bindToBoard(checkDiagonal,
                                                                                          player) or bindToBoard(
            checkInverseDiagonal, player) or bindToBoard(checkFullBoard, player):
        print(player + " has won! Game Over.")
    else:
        try:
            row = int(input(player + rowmess))
            assert row >= 0
            assert row < 3
        except ValueError:
            print("Row must be an integer.")
            handlePlayerInput(player)
        except AssertionError:
            invalidInput = True

        while invalidInput:
            print("Invalid input.")
            row = int(input(player + rowmess))
            if row >= 0 and row < 3:
                invalidInput = False

        try:
            col = int(input(player + colmess))
            assert col >= 0
            assert col < 3
        except ValueError:
            print("Column must be an integer.")
            handlePlayerInput(player)
        except AssertionError:
            invalidInput = True

        while invalidInput:
            print("Invalid input.")
            col = int(input(player + colmess))
            if col >= 0 and col < 3:
                invalidInput = False
        checkDuplicates(player, row, col)
    return row, col


def handlePlayer(player):
    assert player == "player1" or player == "player2"

    if player == "player1":
        try:
            if selectedPieces[player] == None:
                player1piece = str(input(player + piecetype))
                assert player1piece == 'x' or player1piece == 'o'
                selectedPieces[player] = player1piece
        except AssertionError:
            print("Pieces must only be x or o.")
            handlePlayer(player)

        try:
            row, col = handlePlayerInput(player)
            try:
                assert board[row][col] == '-'
                board[row][col] = player1piece
            except AssertionError:
                print("Spot occupied already.")
                handlePlayerInput(player)
        except:
            pass
    elif player == "player2":
        try:
            if selectedPieces[player] == None:
                player2piece = str(input(player + piecetype))
                assert player2piece == 'x' or player2piece == 'o'
                assert selectedPieces["player1"] != player2piece

                selectedPieces[player] = player2piece
        except AssertionError:
            print("Pieces must only be x or o. Pieces also can not be the same as the previous player.")
            handlePlayer(player)

        try:
            row, col = handlePlayerInput(player)
            try:
                assert board[row][col] == '-'
                board[row][col] = player2piece
            except AssertionError:
                print("Spot occupied already.")
                handlePlayerInput(player)
        except:
            pass

    # isGameRunning = False

    bindToBoard(resetBoard)


while isGameRunning:
    if not selectedPieces["player1"] == None and not selectedPieces["player2"] == None:
        handlePlayerInput("player1")
        handlePlayerInput("player2")
    else:
        handlePlayer("player1")
        handlePlayer("player2")

    bindToBoard(printBoard)
