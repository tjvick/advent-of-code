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

for line in strings:
    print(line)
    m = re.match(r'Card\s+(\d+): (.+) \| (.+)', line)
    card_id, scratched, winning = m.groups()
    scratched_numbers = set(int(x) for x in scratched.split())
    winning_numbers = set(int(x) for x in winning.split())

    winners = scratched_numbers.intersection(winning_numbers)
    if len(winners):
        score = 2**(len(winners)-1)
    else:
        score = 0

    print(score)
    total_score += score

print(total_score)
