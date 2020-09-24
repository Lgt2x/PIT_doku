import sys
from grid import SudokuGrid

# python -i src/play_sudoku.py sudoku_db.txt 4

if len(sys.argv) == 3:
    grid = SudokuGrid.from_file(sys.argv[1], int(sys.argv[2]))
else:
    grid = SudokuGrid.from_stdin()

while len(grid.get_empty_pos()):
    print(grid)

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
        if grid.grid[row][col]:
            input_ok = False
    else:
        input_ok = False

    if not input_ok:
        print("mauvais input")
        continue

    grid.write(row, col, val)
