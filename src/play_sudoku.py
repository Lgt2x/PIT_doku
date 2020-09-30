from grid import *
from solver import *
import sys

def play():
    askPlayer = input("Do You wanna Start Playing ?: Yes or Not")
    if askPlayer == "Yes":
        askPlayerModel = input("Do You wanna play with your own grid ?: Yes or Not")
        if askPlayerModel == "Yes":
            NewSudoku = SudokuGrid.from_stdin()
        elif askPlayerModel == "No":
            askFile = input("Saisir Un fichier Source :")
            askLine = input("Saisir la ligne génératrice de la grille:")
            NewSudoku = SudokuGrid.from_file(askFile, askLine)
        else:
            print("Entrer Yes or No")

    return NewSudoku

def run(Sudoku):

    while len(Sudoku.get_empty_pos()) != 0:

        print(Sudoku)

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
            if Sudoku.grid[row][col] != 0:
                input_ok = False
                print("Cette case possède déjà une valeur.")
        else:
            input_ok = False
            print("Vous n'avez pas entré des chiffres.")

        if not input_ok:
            print("mauvais input")
            continue

        Sudoku.write(row, col, val)

        Solve = input("Voulez-vous resoudre le game : Yes or Not")
        if Solve == "Yes":
            Solver = SudokuSolver(Sudoku)
            Solver.solve()
            print(Sudoku)



if __name__ == '__main__':

    NewGame = play()
    run(NewGame)










