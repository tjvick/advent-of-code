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

total_points = 0
for s in strings:
    [opp, me] = s.split()
    selection_points = 3
    if me == 'X':
        selection_points = 1
    if me == 'Y':
        selection_points = 2

    outcome_points = 0
    if (me == 'X' and opp == 'C') or (me == 'Y' and opp == 'A') or (me == 'Z' and opp == 'B'):
        outcome_points = 6
    elif (me == 'X' and opp == 'A') or (me == 'Y' and opp == 'B') or (me == 'Z' and opp == 'C'):
        outcome_points = 3

    round_points = selection_points + outcome_points
    print(round_points)
    total_points += round_points

print(total_points)
