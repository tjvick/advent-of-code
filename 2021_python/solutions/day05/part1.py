from solutions import helpers
import numpy as np
import re

filename = 'input'

strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

filled = {}

for string in strings:
    splits = string.split(' ')
    [x1, y1] = list(map(int, splits[0].split(',')))
    [x2, y2] = list(map(int, splits[2].split(',')))
    print(x1, y1, x2, y2)

    if x1 == x2:
        print('xs')
        for y in range(min((y1, y2)), max((y1, y2))+1, 1):
            if (x1, y) not in filled:
                filled[(x1, y)] = 0
            filled[(x1, y)] += 1
    elif y1 == y2:
        print('ys')
        for x in range(min((x1, x2)), max((x1, x2))+1, 1):
            if (x, y1) not in filled:
                filled[(x, y1)] = 0
            filled[(x, y1)] += 1

print(filled)

count = 0
for key, value in filled.items():
    if value >= 2:
        count += 1

print(count)
