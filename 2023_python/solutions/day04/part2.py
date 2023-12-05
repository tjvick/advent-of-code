from collections import defaultdict

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

card_copies = defaultdict(lambda: 1)

for line in strings:
    m = re.match(r'Card\s+(\d+): (.+) \| (.+)', line)
    card_id, scratched, winning = m.groups()

    card_idx = int(card_id)
    n_copies_of_this_card = card_copies[card_idx]

    scratched_numbers = set(int(x) for x in scratched.split())
    winning_numbers = set(int(x) for x in winning.split())

    winners = scratched_numbers.intersection(winning_numbers)
    print(len(winners))

    for ix in range(len(winners)):
        card_copies[card_idx + ix + 1] += n_copies_of_this_card

print(sum(card_copies.values()))
