from grid import SudokuGrid
from solver import SudokuSolver


def play():
    ask_player = input("Do You wanna Start Playing ?: Yes or No \n")
    keep_playing = True
    while keep_playing:
        if ask_player == "Yes":
            ask_playermodel = input("Do You wanna play with your own grid ?: Yes or No \n")
            if ask_playermodel == "Yes":
                new_sudoku = SudokuGrid.from_stdin()
                keep_playing = False
            elif ask_playermodel == "No":
                ask_file = input("Enter a source file: \n")
                ask_line = input("Which Line do you select for generating your grid ?: \n")
                new_sudoku = SudokuGrid.from_file(ask_file, ask_line)
                keep_playing = False
        elif ask_player == "No":
            exit()
        else:
            ask_player = input("Do You wanna Start Playing ?: Yes or No \n")


    return new_sudoku


def run(sudoku):

    while len(sudoku.get_empty_pos()) != 0:

        print(sudoku)

        row = input("Row : ")
        col = input("Column : ")
        val = input("Value : ")

        input_ok = True
        if row.isdigit() and col.isdigit():
            row = int(row)
            col = int(col)
            val = int(val)

            if not (0 <= row <= 8 and 0 <= col <= 8 and 1 <= val <= 9):
                input_ok = False
                print("Column and Line must lie between the range 0 to 8 and the value between the range 1 to 9.")
            if sudoku.grid[row][col] != 0:
                input_ok = False
                print("The box you selected already has a value.")
        else:
            input_ok = False
            print("You did not enter numbers.")

        if not input_ok:
            print("Wrong input")
            continue

        sudoku.write(row, col, val)

        solve = input("Do you want to game to be resolved : Yes or No \n")
        if solve == "Yes":
            solver = solver(sudoku)
            solver.solve()
            print(sudoku)


if __name__ == '__main__':

    NewGame = play()
    run(NewGame)

