from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

char_sequences = np.array(helpers.read_each_line_as_char_sequence(filename))


char_map = {
    "|": {
        (1, 0): (1, 0),
        (-1, 0): (-1, 0)
    },
    "-": {
        (0, 1): (0, 1),
        (0, -1): (0, -1)
    },
    "L": {
        (1, 0): (0, 1),
        (0, -1): (-1, 0),
    },
    "J": {
        (0, 1): (-1, 0),
        (1, 0): (0, -1)
    },
    "7": {
        (0, 1): (1, 0),
        (-1, 0): (0, -1)
    },
    "F": {
        (-1, 0): (0, 1),
        (0, -1): (1, 0)
    }
}

s_loc_array = np.where(char_sequences == 'S')
s_loc = (s_loc_array[0][0], s_loc_array[1][0])
print(s_loc)

starting_direction_options = [(1, 0), (-1, 0), (0, -1), (0, 1)]
starting_location = s_loc

for starting_direction in starting_direction_options:
    loop = [starting_location]
    current_location = np.array(starting_location)
    direction = np.array(starting_direction)
    loop_found = False

    while True:
        print("current_location", current_location)

        new_location = tuple(current_location + direction)
        character_at_new_location = char_sequences[new_location]

        end = False
        if character_at_new_location in char_map:
            mapping = char_map[character_at_new_location]
            if tuple(direction) in mapping:
                new_direction = mapping[tuple(direction)]
            else:
                end = True
        else:
            end = True

        print('new location', new_location)
        print(character_at_new_location)
        print('end:', end)

        if end:
            if character_at_new_location == 'S':
                print("done!")
                print(loop)
                loop_found = True
            break

        print('new_direction', new_direction)

        loop.append(new_direction)
        direction = np.array(new_direction)
        current_location = np.array(new_location)

    if loop_found:
        break

print(loop)
print(len(loop) / 2)
