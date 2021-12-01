board = [

    ['-', '-', '-'],

    ['-', '-', '-'],

    ['-', '-', '-'],

]

piecetype = "Pick your piece:"
rowmess = "select your row:"
colmess = "select your column:"

player1piece = None
player2piece = None

player1piece = str(input("player1"+ piecetype))
row = int(input("player1" + rowmess))
col = int(input("player1" + colmess))
board[row][col] = player1piece

player2piece = str(input("player2"+ piecetype))
row = int(input("player2" + rowmess))
col = int(input("player2" + colmess))
board[row][col] = player2piece
print(board)

