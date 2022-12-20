from solutions import helpers
import numpy as np
import re
from collections import Counter

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

# 3128 is too high
# 1996

int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename, delimiter=',')


cubes = {tuple(int_sequence) for int_sequence in int_sequences}

exposed_cubes = list()
for cube in cubes:
    for side in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        cube_to_search_for = tuple(np.array(cube) + np.array(side))
        if cube_to_search_for not in cubes:
            exposed_cubes.append(cube_to_search_for)

print(exposed_cubes)

c = Counter(exposed_cubes)
print(c.most_common())

cubes_surrounded_completely = [val for val, count in c.most_common() if count == 6]
print(cubes_surrounded_completely)
print(len(cubes_surrounded_completely))

spaces_bordering_cubes = set(exposed_cubes)

total_sides_to_subtract = 0
for space_bordering_cubes in spaces_bordering_cubes:
    connected_cubes = set()
    unexpanded_cubes = [space_bordering_cubes]
    subtract = True
    while unexpanded_cubes:
        cube = unexpanded_cubes.pop()
        for side in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            cube_to_search_for = tuple(np.array(cube) + np.array(side))
            if cube_to_search_for not in cubes:
                if cube_to_search_for not in connected_cubes:
                    unexpanded_cubes.append(cube_to_search_for)
                connected_cubes.add(cube_to_search_for)

        if len(connected_cubes) > len(cubes):
            subtract = False
            break

    # print(space_bordering_cubes)
    # print(connected_cubes)
    # print(subtract)
    if subtract:
        total_sides_to_subtract += c[space_bordering_cubes]

print(total_sides_to_subtract)
print(len(exposed_cubes))
print(len(exposed_cubes) - total_sides_to_subtract)


