from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
filename = 'test'

int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename, delimiter=',')


cubes = {tuple(int_sequence) for int_sequence in int_sequences}

n_exposed_sides = 0
for cube in cubes:
    for side in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        cube_to_search_for = tuple(np.array(cube) + np.array(side))
        if cube_to_search_for not in cubes:
            n_exposed_sides += 1

print(n_exposed_sides)
