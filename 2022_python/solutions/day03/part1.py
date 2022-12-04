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
total_score = 0
for string in strings:
    n = len(string)//2
    compartment1 = string[0:n]
    compartment2 = string[n:]
    common = set(compartment1).intersection(compartment2)
    print(common)
    letter = common.pop()
    if letter.upper() == letter:
        score = ord(letter) - ord('A') + 27
    else:
        score = ord(letter) - ord('a') + 1

    total_score += score

print(total_score)



