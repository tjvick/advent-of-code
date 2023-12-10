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

starting_direction_options = [(1, 0), (-1, 0), (0, -1), (0, 1)]
starting_location = s_loc

for starting_direction in starting_direction_options:
    loop = [starting_location]
    current_location = np.array(starting_location)
    direction = np.array(starting_direction)
    loop_found = False

    while True:
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

        if end:
            if character_at_new_location == 'S':
                loop_found = True
            break


        loop.append(new_location)
        direction = np.array(new_direction)
        current_location = np.array(new_location)

    if loop_found:
        break


print(loop)
S_char = 'L'
# S_char = '7'

height, width = char_sequences.shape

n_inside = 0

for ir, row in enumerate(char_sequences):
    for ic, _ in enumerate(row):
        print('location under consideration', ir, ic)
        if (ir, ic) in loop:
            continue
        n_tops_crossed = 0
        n_bottoms_crossed = 0
        for ix in range(width - ic - 1):
            search_spot = (ir, ic + ix + 1)
            spot_in_loop = search_spot in loop
            # print('search spot', search_spot)
            # print('char here', char_sequences[search_spot])
            # print('char in loop', spot_in_loop)
            # print(ir, ic + ix + 1)
            if spot_in_loop:
                char = char_sequences[search_spot]
                if char in 'LJ|':
                    n_tops_crossed += 1
                if char in '7F|':
                    n_bottoms_crossed += 1
                if char == 'S':
                    if S_char in 'LJ|':
                        n_tops_crossed += 1
                    if S_char in '7F|':
                        n_bottoms_crossed += 1


        # print('tops, bottoms', n_tops_crossed, n_bottoms_crossed)
        if (n_tops_crossed % 2 == 0) and (n_bottoms_crossed % 2 == 0):
            is_inside = False
        else:
            is_inside = True
            n_inside += 1
        # print("is_inside", is_inside)

print('n_inside:', n_inside)
