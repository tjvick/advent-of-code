from collections import defaultdict

from solutions import helpers
import numpy as np
import re

# filename = 'input'
# strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

# x_bounds = [20, 30]
# y_bounds = [-10, -5]
x_bounds = [211, 232]
y_bounds = [-124, -69]


def simulate(v_0):
    # print("simulating with v0", v_0)
    v = v_0.copy()
    p = np.array([0, 0])
    max_height = 0
    while True:
        p += v
        v[0] = v[0] - np.sign(v[0])
        v[1] -= 1
        if p[1] > max_height:
            max_height = p[1]

        if x_bounds[0] <= p[0] <= x_bounds[1] and y_bounds[0] <= p[1] <= y_bounds[1]:
            # print('LANDED! at', p)
            # print(max_height)
            return max_height

        if v[0] == 0 and p[0] < x_bounds[0]:
            # print('stopped short')
            return -3

        if p[0] > x_bounds[1]:
            # print("too far")
            return -1

        if p[1] < y_bounds[0]:
            # print('too low')
            return -2



count_landings = 0
for ix in range(x_bounds[1]+1):
    for iy in range(y_bounds[0], 200):
        result = simulate(np.array([ix, iy]))
        if result >= 0:
            count_landings += 1


print(count_landings)

# not 4950
# 200: 2032
# 300: 2032

