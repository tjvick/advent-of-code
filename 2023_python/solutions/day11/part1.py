from itertools import combinations

from solutions import helpers
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

char_sequences = helpers.read_each_line_as_char_sequence(filename)

image = np.array(char_sequences)

row_sizes = [1 + all(row == '.') for row in image]
col_sizes = [1 + all(col == '.') for col in image.transpose()]

x = np.where(image == '#')
galaxy_locations = list(zip(*x))

print(galaxy_locations)

combos = combinations(galaxy_locations, 2)

total_distance = 0

for combo in combos:
    print(combo)
    a, b = combo
    a_r, a_c = a
    b_r, b_c = b

    min_r, max_r = min(a_r, b_r), max(a_r, b_r)
    min_c, max_c = min(a_c, b_c), max(a_c, b_c)
    expanded_row_distance = sum(row_sizes[min_r:max_r])
    expanded_col_distance = sum(col_sizes[min_c:max_c])
    print('rows', expanded_row_distance)
    print('cols', expanded_col_distance)

    print(combo, ':', expanded_row_distance + expanded_col_distance)

    total_distance += expanded_row_distance + expanded_col_distance

print("TOTAL: ", total_distance)
