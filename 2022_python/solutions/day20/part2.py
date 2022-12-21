from copy import deepcopy

from solutions import helpers
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

ints = helpers.read_each_line_as_int(filename)

ints *= 811589153

original_ordering = list(enumerate(ints))
zero_number = next((ix, number) for ix, number in original_ordering if number == 0)
n = len(original_ordering)

modified_ordering = deepcopy(original_ordering)
for iy in range(10):
    for ix, number in original_ordering:
        current_position = modified_ordering.index((ix, number))
        new_position = (current_position + number) % (n-1)
        modified_ordering.pop(current_position)
        if new_position > current_position:
            modified_ordering.insert(new_position, (ix, number))
        else:
            modified_ordering.insert(new_position, (ix, number))


zero_location = modified_ordering.index(zero_number)
sum = 0
for ix in [1000, 2000, 3000]:
    val = modified_ordering[(zero_location + ix) % n]
    print(ix, val[1])
    sum += val[1]

print(sum)

# not -1165
# less than 6733