from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

# strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

neighbors = {
    (0, 0): [(0, 1)],
    (0, 1): [(0, 0), (0, 2)],
    (0, 2): [(0, 1), (1, 2), (0, 3)],
    (0, 3): [(0, 2), (0, 4)],
    (0, 4): [(0, 3), (0, 5), (1, 4)],
    (0, 5): [(0, 4), (0, 6)],
    (0, 6): [(0, 5), (0, 7), (1, 6)],
    (0, 7): [(0, 6), (0, 8)],
    (0, 8): [(0, 7), (0, 9), (1, 8)],
    (0, 9): [(0, 8), (0, 10)],
    (0, 10): [(0, 9)],
    (1, 2): [(0, 2), (2, 2)],
    (2, 2): [(1, 2)],
    (1, 4): [(0, 4), (2, 4)],
    (2, 4): [(1, 4)],
    (1, 6): [(0, 6), (2, 6)],
    (2, 6): [(1, 6)],
    (1, 8): [(0, 8), (2, 8)],
    (2, 8): [(1, 8)],
}

# positions = {
#     'A1': (1, 2),
#     'B1': (2, 2),
#     'D1': (1, 4),
#     'C1': (2, 4),
#     'A2': (1, 6),
#     'D2': (2, 6),
#     'B2': (1, 8),
#     'C2': (2, 8)
# }

# test
positions = {
    'B1': (1, 2),
    'A1': (2, 2),
    'C1': (1, 4),
    'D1': (2, 4),
    'B2': (1, 6),
    'C2': (2, 6),
    'D2': (1, 8),
    'A2': (2, 8)
}

destination_columns = {
    'A1': 2,
    'B1': 4,
    'D1': 8,
    'C1': 6,
    'A2': 2,
    'D2': 8,
    'B2': 4,
    'C2': 6
}

print(positions)



'''
test
D: 2  2000
B: 4  40
C: 4  400
A: 3  3
D: 3  3000
D: 7  7000
B: 3  30
B: 
A: 8  8

input
B: 6
C: 3
D: 7
A: 2
D: 5
C: 5

A: 2
A: 



'''

'''
A: 1
B: 10
C: 100
D: 1000

hallway - empty
side rooms - full

locations of each amphipod
walls #
open space .

A - D sorted left to right

never stop on the space immediately outside any room
Never move from the hallway into a room unless that room is their destination and that room contains no amphipods which do not also have that room as their destination room
Once in a hallway, stay in that spot until it can move into a room

12521

'''