from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

data = helpers.read_as_2d_array_of_characters(filepath)

directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
    [1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1]
]

letters = 'XMAS'

xmas_count = 0

for ix_row, row in enumerate(data):
    for ix_col, element in enumerate(row):
        if element == 'X':
            for direction in directions:
                is_xmas = True
                for ix_letter in range(1, 4):
                    x = ix_row + direction[0] * ix_letter
                    y = ix_col + direction[1] * ix_letter
                    if (
                            (x < 0 or x >= data.shape[0]) or
                            (y < 0 or y >= data.shape[1]) or
                            (data[x, y] != letters[ix_letter])
                    ):
                        is_xmas = False
                        break

                if is_xmas:
                    xmas_count += 1

print(xmas_count)

