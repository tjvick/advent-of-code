from collections import defaultdict

from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

cubes = defaultdict(int)

pattern = re.compile('(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
for row in strings:
    m = pattern.match(row)
    is_on, xmin, xmax, ymin, ymax, zmin, zmax = m.groups()
    is_on = is_on == 'on'
    xmin, xmax, ymin, ymax, zmin, zmax = list(map(int, [xmin, xmax, ymin, ymax, zmin, zmax]))
    print(xmin, xmax, ymin, ymax, zmin, zmax)

    if xmin >= -50 and xmax <= 50 and ymin >= -50 and ymax <= 50 and zmin >= -50 and zmax <= 50:
        for ix in range(xmin, xmax+1):
            for iy in range(ymin, ymax+1):
                for iz in range(zmin, zmax+1):
                    cubes[(ix, iy, iz)] = is_on


print(sum(cubes.values()))

