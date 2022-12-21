from copy import deepcopy

from solutions import helpers
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test2'

ints = helpers.read_each_line_as_int(filename)


original_ordering = list(enumerate(ints))
n = len(original_ordering)

new_positions = []

modified_ordering = deepcopy(original_ordering)
for ix, number in original_ordering:
    # print(modified_ordering)
    current_position = modified_ordering.index((ix, number))
    new_position = (current_position + number) % (n-1)
    new_positions.append(new_position)
    # print(number, current_position, new_position)
    modified_ordering.pop(current_position)
    if new_position > current_position:
        modified_ordering.insert(new_position, (ix, number))
    else:
        modified_ordering.insert(new_position, (ix, number))

print(modified_ordering)
print(new_positions)

zero_location = next(pos for pos, number in enumerate(modified_ordering) if number[1] == 0)
sum = 0
for ix in [1000, 2000, 3000]:
    val = modified_ordering[(zero_location + ix) % n]
    print(ix, val[1])
    sum += val[1]

print(sum)

# not -1165
# less than 6733