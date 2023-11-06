import numpy as np
board = np.zeros((3, 3))
player = 1

def check_win(player):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True
    return False

while True:
    print(board)
    row, col = map(int, input(f"Player {player}'s turn (row col): ").split())
    if board[row][col] != 0:
        print("Invalid move. Try again.")
        continue
    board[row][col] = player
    if check_win(player):
        print(f"Player {player} wins!")
        break
    if np.all(board != 0):
        print("It's a tie!")
        break
    player = 3 - player