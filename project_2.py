"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Marek Hes
email: marekhes99@centrum.cz
discord: marek_09805
"""
# import 
from ttt_extension import rules
from ttt_extension import game_board
from ttt_extension import winner_check

# výpis pravidel
print(rules)
board = []
for _ in range(3):
    line = []
    for _ in range(3):
        line.append(" ")
    board.append(line)
# výpis prázdného herního pole před prvním tahem
game_board(board)

# definice herního mechanismu tic tac toe
def tic_tac_toe():
    player = "o"
    moves = 0
    # určení počtu jednotlivých kroků ve hře
    while moves < 9:
        move = input(f"Player {player} | Please enter your move number: ")
        # rozhodování, zda-li uživatelem zadaný krok ve hře je číslo
        if move.isdigit():
            move = int(move)
            # určení intervalu čísel, které jsou mimo herní pole
            if move == 0 or move > 9:
                print("Invalid move! Please enter a number between 1 and 9.")
                continue
            # získání řádku a sloupce na základě čísla tahu hráče
            row, col = divmod(move - 1, 3)
            if board[row][col] == " ":
                # umístění hráčovy značky na desku
                board[row][col] = player
                game_board(board)
                # winner_check - uživatelem definovaná funkce rozhodující o vítězství
                if winner_check(board, player):
                    print("=" * 40)
                    print(f"Congratulations, the player {player} WON!")
                    print("=" * 40)
                    break
                # střídání tahů hráče "o" a hráče "x"
                if player == "o":
                    player = "x"
                else:
                    player = "o"
                moves += 1
            else:
                print("The field you've chosen has already been taken. Please enter different number.")
        else:
            print("Invalid move! Please enter a number between 1 and 9.")
    # rozhodnutí o remíze
    if moves == 9:
        print("=" * 40)
        print("It's a draw!")
        print("=" * 40)

#spuštění funkce za předpokladu, že je tento program hlavním programem
if __name__ == "__main__":
    tic_tac_toe()


