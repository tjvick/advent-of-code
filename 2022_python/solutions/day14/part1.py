from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

all_rock_paths = []
for string in strings:
    rock_path = [np.array(eval(section)) for section in string.replace(' ', '').split('->')]
    all_rock_paths.append(rock_path)


rock_grid = set()


def add_to_grid(point):
    x, y = tuple(point)
    rock_grid.add((int(x), int(y)))


for rock_path in all_rock_paths:
    for ix_section in range(len(rock_path) - 1):
        a = rock_path[ix_section]
        b = rock_path[ix_section+1]

        add_to_grid(a)
        add_to_grid(b)

        distance = sum(b-a)
        delta = (b - a) / distance
        for step in range(abs(distance)):
            new_rock = a + (step+1)*np.sign(distance)*delta
            add_to_grid(new_rock)

        print(a, b, b-a, distance)


lowest_point = max(y for x, y in rock_grid)
print(lowest_point)

sand_grid = set()
falling_forever = False
counter = 0
while not falling_forever:
    sand_location = np.array([500, 0])
    while True:
        down_spot = tuple(sand_location + [0, 1])
        down_left_spot = tuple(sand_location + [-1, 1])
        down_right_spot = tuple(sand_location + [1, 1])
        if down_spot in rock_grid or down_spot in sand_grid:
            if down_left_spot in rock_grid or down_left_spot in sand_grid:
                if down_right_spot in rock_grid or down_right_spot in sand_grid:
                    # come to rest
                    sand_grid.add(tuple(sand_location))
                    break
                else:
                    # move down and right
                    sand_location = np.array(down_right_spot)
            else:
                # move down and left
                sand_location = np.array(down_left_spot)
        else:
            sand_location = np.array(down_spot)
            if sand_location[1] > lowest_point:
                print("Falling forever after", counter)
                falling_forever = True
                break

    counter += 1


print(sand_grid)

