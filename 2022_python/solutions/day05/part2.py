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

stacking = []
instructions = []
on_instructions = False
for string in strings:
    if string == '':
        on_instructions = True
        continue

    if on_instructions:
        instructions.append(string)
    else:
        stacking.append(string)

crates = np.empty((9, 9), dtype=str)
for ist, stack in enumerate(stacking):
    for ix in range(9):
        try:
            crate = stack[ix*4+1]
            crates[ix, ist] = crate
        except:
            pass

stacks = []
for row in crates:
    stacks.append([x for x in row if x.replace(' ', '')])

print(stacks)

print(instructions)
for instruction in instructions:
    m = re.match('move (\d+) from (\d+) to (\d+)', instruction)
    count = int(m.group(1))
    source = int(m.group(2))
    dest = int(m.group(3))

    grabbed = stacks[source-1][0:count]
    for x in range(count):
        stacks[source-1].pop(0)

    for crate in reversed(grabbed):
        stacks[dest-1].insert(0, crate)

    print(stacks)


print(''.join(stack[0] for stack in stacks))

