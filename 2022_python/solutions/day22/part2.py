import dataclasses
from collections import defaultdict
from enum import Enum
from dataclasses import dataclass, replace
from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

CUBE_SIZE = 50
# CUBE_SIZE = 4

char_sequences = helpers.read_each_line_as_char_sequence(filename)

wall_map = {}
map_complete = False
instructions = ''
for irow, char_sequence in enumerate(char_sequences):
    if map_complete:
        instructions = ''.join(char_sequence)
    elif char_sequence == []:
        map_complete = True
    else:
        for icol, char in enumerate(char_sequence):
            if char in ".#":
                wall_map[(irow, icol)] = False if char == "#" else True

distances_list = [int(x) for x in re.split(r'R|L', instructions)]
directions_list = list(''.join(re.split(r'\d+', instructions)))
# print(directions_list)
distances = iter(distances_list)
directions = iter(directions_list)

# right, down, left, up
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
facings = [(0, 1), (1, 0), (0, -1), (-1, 0)]


edge_stitching = defaultdict(dict)


def make_edge(rows, cols):
    if isinstance(rows, tuple):
        r = range(rows[0], rows[1], np.sign(rows[1]-rows[0]))
    else:
        r = [rows] * CUBE_SIZE

    if isinstance(cols, tuple):
        c = range(cols[0], cols[1], np.sign(cols[1]-cols[0]))
    else:
        c = [cols] * CUBE_SIZE

    return list(zip(r, c))


# edge_specs = [
#     (RIGHT, (0, 1*CUBE_SIZE), 3*CUBE_SIZE-1, LEFT, (3*CUBE_SIZE-1, 2*CUBE_SIZE-1), 4*CUBE_SIZE-1),
#     (RIGHT, (1*CUBE_SIZE, 2*CUBE_SIZE), 3*CUBE_SIZE-1, DOWN, 2*CUBE_SIZE, (4*CUBE_SIZE-1, 3*CUBE_SIZE-1)),
#     (DOWN, 3*CUBE_SIZE-1, (2*CUBE_SIZE, 3*CUBE_SIZE), UP, 2*CUBE_SIZE-1, (1*CUBE_SIZE-1, 0*CUBE_SIZE-1)),
#     (DOWN, 3*CUBE_SIZE-1, (3*CUBE_SIZE, 4*CUBE_SIZE), RIGHT, (2*CUBE_SIZE-1, 1*CUBE_SIZE-1), 0),
#     (UP, 1*CUBE_SIZE, (1*CUBE_SIZE, 2*CUBE_SIZE), RIGHT, (0*CUBE_SIZE, 1*CUBE_SIZE), 2*CUBE_SIZE),
# ]
edge_specs = [
    (RIGHT, (0*CUBE_SIZE, 1*CUBE_SIZE), 3*CUBE_SIZE-1, LEFT, (3*CUBE_SIZE-1, 2*CUBE_SIZE-1), 2*CUBE_SIZE-1),
    (RIGHT, (1*CUBE_SIZE, 2*CUBE_SIZE), 2*CUBE_SIZE-1, UP, 1*CUBE_SIZE-1, (2*CUBE_SIZE, 3*CUBE_SIZE)),
    (RIGHT, (3*CUBE_SIZE, 4*CUBE_SIZE), 1*CUBE_SIZE-1, UP, 3*CUBE_SIZE-1, (1*CUBE_SIZE, 2*CUBE_SIZE)),
    (DOWN, 4*CUBE_SIZE-1, (0*CUBE_SIZE, 1*CUBE_SIZE), DOWN, 0*CUBE_SIZE, (2*CUBE_SIZE, 3*CUBE_SIZE)),
    (DOWN, 4*CUBE_SIZE-1, (0*CUBE_SIZE, 1*CUBE_SIZE), DOWN, 0*CUBE_SIZE, (2*CUBE_SIZE, 3*CUBE_SIZE)),
    (UP, 2*CUBE_SIZE, (0*CUBE_SIZE, 1*CUBE_SIZE), RIGHT, (1*CUBE_SIZE, 2*CUBE_SIZE), 1*CUBE_SIZE),
    (UP, 0*CUBE_SIZE, (1*CUBE_SIZE, 2*CUBE_SIZE), RIGHT, (3*CUBE_SIZE, 4*CUBE_SIZE), 0*CUBE_SIZE),
    (LEFT, (0*CUBE_SIZE, 1*CUBE_SIZE), 1*CUBE_SIZE, RIGHT, (3*CUBE_SIZE-1, 2*CUBE_SIZE-1), 0*CUBE_SIZE),
]
for edge_spec in edge_specs:
    facing1, rows1, cols1, facing2, rows2, cols2 = edge_spec
    row_col_pairs_1 = make_edge(rows1, cols1)
    row_col_pairs_2 = make_edge(rows2, cols2)
    edge_stitching[facing1] |= {rc1: (rc2, facing2) for rc1, rc2 in zip(row_col_pairs_1, row_col_pairs_2)}

    opposite_facing1 = (facing1 + 2) % 4
    opposite_facing2 = (facing2 + 2) % 4
    edge_stitching[opposite_facing2] |= {rc2: (rc1, opposite_facing1) for rc2, rc1 in zip(row_col_pairs_2, row_col_pairs_1)}


# print(dict(edge_stitching[0]))
print(dict(edge_stitching[3]))


@dataclass
class Facing:
    ix: int = 0

    @property
    def facing(self):
        return np.array(facings[self.ix])

    def turn_right(self):
        self.ix = (self.ix + 1) % 4
        return self

    def turn_left(self):
        self.ix = (self.ix - 1) % 4
        return self


def find_wraparound_position(cur_position, cur_facing):
    new_position, new_facing = edge_stitching[cur_facing.ix][tuple(cur_position)]
    # print("Returning", new_position)
    return new_position, new_facing


starting_point = np.array(list(wall_map.keys())[0])

current_position = starting_point
current_facing = Facing(ix=0)
# print(current_position)

try:
    while True:
        distance = next(distances)

        for ix in range(distance):
            possible_next_position = current_position + current_facing.facing
            if tuple(possible_next_position) in wall_map:
                if wall_map[tuple(possible_next_position)]:
                    current_position = possible_next_position
                    # print(current_position)
                else:
                    break
            else:
                # print("Before searching...", current_facing.facing)
                possible_next_position, possible_next_facing = find_wraparound_position(current_position, current_facing)
                # print("After searching...", current_facing.facing)
                if wall_map[tuple(possible_next_position)]:
                    current_position = possible_next_position
                    current_facing.ix = possible_next_facing
                    # print(current_position)
                else:
                    # print("Wall at wraparound position")
                    break

        turn_direction = next(directions)
        if turn_direction == "R":
            # print("Turning right")
            current_facing.turn_right()
        else:
            # print("Turning left")
            current_facing.turn_left()
        # print(current_facing.facing)
except StopIteration:
    print(current_position)
    print(current_facing.facing)
    row = current_position[0] + 1
    col = current_position[1] + 1
    facing_index = current_facing.ix
    password = 1000*row + 4*col + facing_index
    print("password:", password)