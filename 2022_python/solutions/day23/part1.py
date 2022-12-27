from collections import defaultdict
from enum import Enum

from solutions import helpers
import numpy as np
from itertools import cycle
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

n_rounds = 10

char_sequences = helpers.read_each_line_as_char_sequence(filename)

elf_positions = {}
elf_counter = 0
for irow, char_sequence in enumerate(char_sequences):
    for icol, char in enumerate(char_sequence):
        if char == "#":
            elf_positions[elf_counter] = (irow, icol)
            elf_counter += 1

print(elf_positions)

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

directions_cycler = cycle([
    [NORTH, SOUTH, WEST, EAST],
    [SOUTH, WEST, EAST, NORTH],
    [WEST, EAST, NORTH, SOUTH],
    [EAST, NORTH, SOUTH, WEST],
])

spaces_to_check = {
    NORTH: [(-1, -1), (-1, 0), (-1, 1)],
    SOUTH: [(1, -1), (1, 0), (1, 1)],
    WEST: [(1, -1), (0, -1), (-1, -1)],
    EAST: [(1, 1), (0, 1), (-1, 1)],
}

spaces_to_move_to = {
    NORTH: (-1, 0),
    SOUTH: (1, 0),
    WEST: (0, -1),
    EAST: (0, 1),
}

for round_number in range(n_rounds):
    # first half
    proposed_positions = defaultdict(list)
    directions_to_consider = next(directions_cycler)
    # print("directions_to_consider", directions_to_consider)
    for elf_id, current_elf_position in elf_positions.items():
        # print("current elf position", current_elf_position)
        is_elf_nearby = False
        for direction in directions_to_consider:
            for space_to_check in spaces_to_check[direction]:
                position_to_check = tuple(np.array(current_elf_position) + np.array(space_to_check))
                if position_to_check in elf_positions.values():
                    is_elf_nearby = True
                    break
            if is_elf_nearby:
                break
        if not is_elf_nearby:
            continue

        for direction in directions_to_consider:
            # print("direction to consider", direction)
            is_direction_open = True
            for space_to_check in spaces_to_check[direction]:
                position_to_check = tuple(np.array(current_elf_position) + np.array(space_to_check))
                if position_to_check in elf_positions.values():
                    is_direction_open = False
                    break
            if is_direction_open:
                # print("propose moving in direction", direction)
                space_to_move_to = spaces_to_move_to[direction]
                new_proposed_position = tuple(np.array(current_elf_position) + np.array(space_to_move_to))
                proposed_positions[new_proposed_position].append(elf_id)
                break

    # second half
    for proposed_position, elf_ids in proposed_positions.items():
        if len(elf_ids) == 1:
            elf_positions[elf_ids[0]] = proposed_position


# elf_positions = {elf_idx: (x, y)}
# proposed_positions = {(x, y): [elf_idx]]}
# print(elf_positions)
min_row = min([row for row, col in elf_positions.values()])
max_row = max([row for row, col in elf_positions.values()])
min_col = min([col for row, col in elf_positions.values()])
max_col = max([col for row, col in elf_positions.values()])
print(min_row, max_row, min_col, max_col)

spaces_in_rectangle = (max_row - min_row + 1)*(max_col - min_col + 1)
empty_spaces_in_rectangle = spaces_in_rectangle - len(elf_positions)
print(empty_spaces_in_rectangle)

# graph_positions = [(row - min_row, col - min_col) for row, col in elf_positions.values()]
# graph_matrix = np.zeros((max_row-min_row+1, max_col-min_col+1), dtype=int)
# for pos in graph_positions:
#     graph_matrix[pos] = 1
#
# for row in graph_matrix:
#     print(''.join(str(x) for x in row))