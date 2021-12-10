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

the_closers = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

illegals = []
total_scores = []
print(char_sequences)
for sequence in char_sequences:
    stack = []
    bad = False
    for char in sequence:
        if char in openers:
            stack.append(char)
        elif stack.pop() == the_openers[char]:
            pass
        else:
            bad = True

    if not bad and len(stack) > 0:
        total_score = 0
        for char in reversed(stack):
            total_score = total_score*5 + points[the_closers[char]]
        print(total_score)
        total_scores.append(total_score)


answer = sum(points[char] for char in illegals)
print(answer)

print(np.median(total_scores))


