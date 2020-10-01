from grid import *
from solver import *


def play():
    ask_player = input("Do You wanna Start Playing ?: Yes or No \n")
    continuer = True
    while continuer:
        if ask_player == "Yes":
            ask_playermodel = input("Do You wanna play with your own grid ?: Yes or No \n")
            if ask_playermodel == "Yes":
                new_sudoku = SudokuGrid.from_stdin()
                continuer = False
            elif ask_playermodel == "No":
                ask_file = input("Saisir Un fichier Source : \n")
                ask_line = input("Saisir la ligne génératrice de la grille: \n")
                new_sudoku = SudokuGrid.from_file(ask_file, ask_line)
                continuer = False
        elif ask_player == "No":
            exit()
        else:
            ask_player = input("Do You wanna Start Playing ?: Yes or No \n")


    return new_sudoku


def run(sudoku):

    while len(sudoku.get_empty_pos()) != 0:

        print(sudoku)

        row = input("Ligne : ")
        col = input("Colonne : ")
        val = input("Valeur : ")

        input_ok = True
        if row.isdigit() and col.isdigit():
            row = int(row)
            col = int(col)
            val = int(val)

            if not (0 <= row <= 8 and 0 <= col <= 8 and 1 <= val <= 9):
                input_ok = False
                print("Colonne et Ligne doivent être compris entre 0 et 8 et La Valeur entre 1 et 9.")
            if sudoku.grid[row][col] != 0:
                input_ok = False
                print("Cette case possède déjà une valeur.")
        else:
            input_ok = False
            print("Vous n'avez pas entré des chiffres.")

        if not input_ok:
            print("mauvais input")
            continue

        sudoku.write(row, col, val)

        solve = input("Voulez-vous resoudre le game : Yes or No \n")
        if solve == "Yes":
            solver = solver(sudoku)
            solver.solve()
            print(sudoku)


if __name__ == '__main__':

    NewGame = play()
    run(NewGame)

