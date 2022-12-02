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

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

total_points = 0
for s in strings:
    [opp, me] = s.split()

    if me == 'X': #lose
        if opp == 'A':
            selection_points = 3 # scis
        if opp == 'B':
            selection_points = 1 # rock
        if opp == 'C':
            selection_points = 2 # paper
    elif me == 'Y': # draw
        if opp == 'A':
            selection_points = 1 # rock
        if opp == 'B':
            selection_points = 2 # paper
        if opp == 'C':
            selection_points = 3 # scis
    else: # win
        if opp == 'A':
            selection_points = 2 # paper
        if opp == 'B':
            selection_points = 3 # sci
        if opp == 'C':
            selection_points = 1 # rock

    outcome_points = 6
    if me == 'X':
        outcome_points = 0
    if me == 'Y':
        outcome_points = 3

    round_points = selection_points + outcome_points
    print(round_points)
    total_points += round_points

print(total_points)
