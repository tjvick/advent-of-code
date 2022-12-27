from collections import defaultdict
from enum import Enum

from solutions import helpers
import numpy as np
from itertools import cycle

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
elf_positions_set = set(elf_positions.values())

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

surrounding_spaces = [
    np.array([-1, 1]),
    np.array([-1, 0]),
    np.array([-1, -1]),
    np.array([1, -1]),
    np.array([1, 0]),
    np.array([1, 1]),
    np.array([0, -1]),
    np.array([0, 1]),
]

spaces_to_move_to = {
    NORTH: (-1, 0),
    SOUTH: (1, 0),
    WEST: (0, -1),
    EAST: (0, 1),
}

round_number = 0
while True:
    # first half
    print(round_number)
    round_number += 1
    proposed_positions = defaultdict(list)
    directions_to_consider = next(directions_cycler)
    for elf_id, current_elf_position in elf_positions.items():
        is_elf_nearby = False
        for surrounding_space in surrounding_spaces:
            position_to_check = tuple(np.array(current_elf_position) + surrounding_space)
            if position_to_check in elf_positions_set:
                is_elf_nearby = True
                break
        if not is_elf_nearby:
            continue

        for direction in directions_to_consider:
            is_direction_open = True
            for space_to_check in spaces_to_check[direction]:
                position_to_check = tuple(np.array(current_elf_position) + np.array(space_to_check))
                if position_to_check in elf_positions_set:
                    is_direction_open = False
                    break
            if is_direction_open:
                space_to_move_to = spaces_to_move_to[direction]
                new_proposed_position = tuple(np.array(current_elf_position) + np.array(space_to_move_to))
                proposed_positions[new_proposed_position].append(elf_id)
                break

    # second half
    if len(proposed_positions) == 0:
        print("NO ELVES MOVED!", round_number)
        break
    for proposed_position, elf_ids in proposed_positions.items():
        if len(elf_ids) == 1:
            elf_positions_set.remove(elf_positions[elf_ids[0]])
            elf_positions[elf_ids[0]] = proposed_position
            elf_positions_set.add(proposed_position)


# 1757 too high