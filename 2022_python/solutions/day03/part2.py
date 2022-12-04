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


def get_score(letter):
    if letter.upper() == letter:
        score = ord(letter) - ord('A') + 27
    else:
        score = ord(letter) - ord('a') + 1

    return score


total_score = 0
for ix in range(len(strings)//3):
    print(ix)
    elf1 = strings[ix*3]
    elf2 = strings[ix*3+1]
    elf3 = strings[ix*3+2]

    common = set(elf1).intersection(set(elf3)).intersection(set(elf2))

    print(common)
    letter = common.pop()
    total_score += get_score(letter)

print(total_score)



