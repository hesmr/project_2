rules = '''Welcome to Tic Tac Toe
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game
--------------------------------------------'''
# hrací pole
def game_board(board):
    print("+---+---+---+")
    for line in board:
        print("| " + " | ".join(line) + " |")
        print("+---+---+---+")

# rozhodování o výhře
def winner_check(board, player):
    # kontrolá řádek
    for line in board:
        winner = True
        for mark in line:
            if mark != player:
                winner = False
                break
        if winner:
            return True
    # kontrola sloupců
    for col in range(3):
        winner = True
        for line in range(3):
            if board[line][col] != player:
                winner = False
                break
        if winner:
            return True
    # kontrola hlavní diagonály
    winner = True
    for i in range(3):
        if board[i][i] != player:
            winner = False
            break
    if winner:
        return True

    # kontrola vedlejší diagonály
    winner = True
    for i in range(3):
        if board[i][2 - i] != player:
            winner = False
            break
    if winner:
        return True

