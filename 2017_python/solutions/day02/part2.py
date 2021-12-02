from solutions import helpers
import numpy as np

filename = 'input'

integer_lists = helpers.read_as_delimited_integer_lists(filename)


def find_factor(integer_list):
    sorted_ints = np.sort(integer_list)
    for ixs, smaller in enumerate(sorted_ints):
        for larger in sorted_ints[ixs + 1:]:
            if larger % smaller == 0:
                return larger / smaller


checksum = sum(find_factor(integer_list) for integer_list in integer_lists)

print(checksum)


