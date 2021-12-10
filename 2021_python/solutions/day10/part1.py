from solutions import helpers
import numpy as np
import re

filename = 'input'

# strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
the_openers = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

illegals = []
print(char_sequences)
for sequence in char_sequences:
    print(sequence)
    stack = []
    for char in sequence:
        if char in openers:
            stack.append(char)
        elif stack.pop() == the_openers[char]:
            # print('good')
            pass
        else:
            print('bad')
            illegals.append(char)


points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
answer = sum(points[char] for char in illegals)
print(answer)


