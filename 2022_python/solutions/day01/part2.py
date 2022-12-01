from solutions import helpers
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

all_cals = []
cals = 0
for s in strings:
    if s == '':
        all_cals.append(cals)
        cals = 0
    else:
        cals += int(s)

all_cals.append(cals)

print(sum(sorted(all_cals, reverse=True)[0:3]))
