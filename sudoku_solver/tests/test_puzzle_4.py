"""
Test file for puzzle_4.
Not yet solved.
"""

import sys
sys.path.append('../')
from sudoku_solver import *


sudoku = Sudoku_Solver()
sudoku.import_board("puzzle_4.txt")
sudoku.print_board()
print('===============================')


# Solve
print('Init reduce:')
sudoku.solve_queue()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Check matching sets:')
sudoku.check_matching_sets()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')


print('Eliminate single-box block-level possibilities:')
sudoku.check_within_boxes()
sudoku.print_board()
# sudoku.print_possible_values()
print('===============================')


print('Multi-boxes block-level eliminations:')
sudoku.check_block_elim()
sudoku.print_board()
sudoku.print_possible_values()
print('===============================')







