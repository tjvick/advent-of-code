from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

# strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

tree_grid = np.array(digit_sequences)

grid_size = tree_grid.shape
total_visible = 0
print(grid_size)
for ir, row in enumerate(tree_grid):
    for ic, tree in enumerate(row):
        print(ir, ic, tree)
        if ic == 0 or ir == 0 or ir == grid_size[0]-1 or ic == grid_size[1]-1:
            visible = True
        elif max(row[ic+1:]) < tree: # to right
            visible = True
        elif max(tree_grid[ir+1:, ic]) < tree: # down:
            visible = True
        elif max(row[:ic]) < tree: # to left
            visible = True
        elif max(tree_grid[:ir, ic]) < tree: # up
            visible = True
        else:
            visible = False
        print(visible)

        total_visible += visible

print(total_visible)





