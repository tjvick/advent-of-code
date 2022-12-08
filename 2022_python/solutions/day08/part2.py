from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

digit_sequences = helpers.read_each_line_as_digit_sequence(filename)

tree_grid = np.array(digit_sequences)
max_scenic_score = 0

grid_size = tree_grid.shape
print(grid_size)
for ir, row in enumerate(tree_grid):
    for ic, tree in enumerate(row):
        print(ir, ic, tree)
        if ic == 0 or ir == 0 or ir == grid_size[0]-1 or ic == grid_size[1]-1:
            # score 0
            continue

        right_score = 0
        for t in row[ic+1:]:
            right_score += 1
            if t >= tree:
                break

        down_score = 0
        for t in tree_grid[ir+1:, ic]:
            down_score += 1
            if t >= tree:
                break

        left_score = 0
        for t in reversed(row[:ic]):
            left_score += 1
            if t >= tree:
                break

        up_score = 0
        for t in reversed(tree_grid[:ir, ic]):
            up_score += 1
            if t >= tree:
                break

        scenic_score = right_score * down_score * left_score * up_score
        print(up_score, left_score, right_score, down_score, scenic_score)
        max_scenic_score = max(max_scenic_score, scenic_score)


print(max_scenic_score)





