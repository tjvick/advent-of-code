from solutions import helpers
import numpy as np

filename = 'input'

integer_lists = helpers.read_as_delimited_integer_lists(filename)

checksum = 0
for integer_list in integer_lists:
    sorted = np.sort(integer_list)
    factor = 0
    for ixs, smaller in enumerate(sorted):
        for larger in sorted[ixs+1:]:
            if larger % smaller == 0:
                factor = larger / smaller
                break

    checksum += factor

print(checksum)


