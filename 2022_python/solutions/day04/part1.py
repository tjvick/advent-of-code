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

overlaps = 0
for string in strings:
    m = re.match('(\d+)-(\d+),(\d+)-(\d+)', string)
    [a,b,c,d] = m.groups()
    A = int(a)
    B = int(b)
    C = int(c)
    D = int(d)
    if (A >= C and B <= D) or (C >= A and D <=B):
        overlaps += 1

print(overlaps)
