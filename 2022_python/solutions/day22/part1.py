import dataclasses
from enum import Enum
from dataclasses import dataclass, replace
from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

# strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

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
print(directions_list)
distances = iter(distances_list)
directions = iter(directions_list)

# right, down, left, up
facings = [(0, 1), (1, 0), (0, -1), (-1, 0)]


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
    temp_facing = Facing(ix=cur_facing.ix)
    temp_facing.turn_right()
    temp_facing.turn_right()
    print(cur_facing.facing, temp_facing.facing)
    new_position = cur_position.copy()
    while tuple(new_position) in wall_map:
        new_position += temp_facing.facing
        print("searching...", new_position)

    print("Too far:", new_position)
    print("Returning", new_position - temp_facing.facing)

    return new_position - temp_facing.facing


starting_point = np.array(list(wall_map.keys())[0])

current_position = starting_point
current_facing = Facing(ix=0)
print(current_position)

try:
    while True:
        distance = next(distances)

        for ix in range(distance):
            possible_next_position = current_position + current_facing.facing
            if tuple(possible_next_position) in wall_map:
                if wall_map[tuple(possible_next_position)]:
                    current_position = possible_next_position
                    print(current_position)
                else:
                    break
            else:
                print("Before searching...", current_facing.facing)
                possible_next_position = find_wraparound_position(current_position, current_facing)
                print("After searching...", current_facing.facing)
                if wall_map[tuple(possible_next_position)]:
                    current_position = possible_next_position
                    print(current_position)
                else:
                    print("Wall at wraparound position")
                    break

        turn_direction = next(directions)
        if turn_direction == "R":
            print("Turning right")
            current_facing.turn_right()
        else:
            print("Turning left")
            current_facing.turn_left()
        # print(current_facing.facing)
finally:
    print(current_position)
    print(current_facing.facing)
    row = current_position[0] + 1
    col = current_position[1] + 1
    facing_index = current_facing.ix
    password = 1000*row + 4*col + facing_index
    print("password:", password)