"""
Test file for puzzle_2.
Can be solved by checking all unique once.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_2.txt")
sudoku.print_board()
print('===============================')


# Solve
print('Init reduce:')
sudoku.init_reduce()
sudoku.print_board()
sudoku.print_possible_values()


print('Unique lookup test:')
sudoku.check_all_unique()
sudoku.print_board()
sudoku.print_possible_values()






