from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

# strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

sequence_stacks = []
for sequence in int_sequences:
    print(sequence)
    sequence_stack = [sequence]
    while True:
        diff = np.diff(sequence)
        sequence_stack.append(diff)
        print(diff)
        if sum(diff) == 0:
            break

        sequence = diff

    print(sequence_stack)
    sequence_stacks.append(sequence_stack)

print(sequence_stacks)
final_values = []
for sequence_stack in sequence_stacks:
    bottom_to_top = list(reversed(sequence_stack))
    amount_to_add = 0
    print('bottom to top', bottom_to_top)
    for sequence in bottom_to_top[1:]:
        value_to_add_to = sequence[-1]
        new_value = value_to_add_to + amount_to_add
        amount_to_add = new_value
    print(new_value)
    final_values.append(new_value)

print(sum(final_values))
