from solutions import helpers
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

char_sequences = helpers.read_each_line_as_char_sequence(filename)

easties = []
southies = []

for row in char_sequences:
    easties.append(list(map(lambda c: c == '>', row)))
    southies.append(list(map(lambda c: c == 'v', row)))

width = len(easties[0])
height = len(easties)

def display(easties_locations, southies_locations):
    display_matrix = np.full([height, width], ".", dtype='str')
    for location in easties_locations:
        display_matrix[location[0], location[1]] = '>'
    for location in southies_locations:
        display_matrix[location[0], location[1]] = 'v'
    for row in display_matrix:
        print(''.join(row))

easties_locations = np.argwhere(easties)
southies_locations = np.argwhere(southies)

# display(easties_locations, southies_locations)

easties_set = set(map(tuple, easties_locations))
southies_set = set(map(tuple, southies_locations))

full_set = set(map(tuple, easties_locations)) | set(map(tuple, southies_locations))

for ix in range(10000):
    if ix % 10 == 0:
        print(ix)
    easties_destinations = (easties_locations + [0, 1]) % [height, width]
    easties_can_move = np.array([dest not in full_set for dest in map(tuple, easties_destinations)])
    easties_locations = np.where(easties_can_move[:, None], easties_destinations, easties_locations)
    full_set = set(map(tuple, easties_locations)) | set(map(tuple, southies_locations))

    southies_destinations = (southies_locations + [1, 0]) % [height, width]
    southies_can_move = np.array([dest not in full_set for dest in map(tuple, southies_destinations)])
    southies_locations = np.where(southies_can_move[:, None], southies_destinations, southies_locations)
    full_set = set(map(tuple, easties_locations)) | set(map(tuple, southies_locations))

    # print('after step ', ix+1)
    # display(easties_locations, southies_locations)

    if sum(easties_can_move) + sum(southies_can_move) == 0:
        print('Answer: ', ix+1)
        break








