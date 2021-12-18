from solutions import helpers
import numpy as np
import re

filename = 'input'

char_sequences = helpers.read_each_line_as_char_sequence(filename)

opener = '['
closer = ']'
def parse_number(char_sequence):
    depth = 0
    vals = []
    depths = []
    for char in char_sequence:
        if char == opener:
            depth += 1
        if char == closer:
            depth -= 1
        if re.match('\d', char):
            vals.append(int(char))
            depths.append(depth-1)

    return vals, depths


def explode(vals, depths):
    target_pair = [(ix, v) for ix, (v, d) in enumerate(zip(vals, depths)) if d >= 4][0:2]

    if target_pair[0][0] > 0:
        ix_value_to_left = target_pair[0][0]-1
        vals[ix_value_to_left] += target_pair[0][1]

    if target_pair[1][0] < len(vals) - 1:
        ix_value_to_right = target_pair[1][0]+1
        vals[ix_value_to_right] += target_pair[1][1]

    depths[target_pair[0][0]] -= 1
    vals[target_pair[0][0]] = 0
    del depths[target_pair[1][0]]
    del vals[target_pair[1][0]]

    return vals, depths


def split(vals, depths):
    ix, v = [(ix, v) for ix, (v, d) in enumerate(zip(vals, depths)) if v >= 10][0]

    left = int(np.floor(v/2))
    right = int(np.ceil(v/2))
    vals[ix] = left
    depths[ix] += 1

    vals.insert(ix+1, right)
    depths.insert(ix+1, depths[ix])

    return vals, depths


def reduce(vals, depths):
    if any(d >= 4 for d in depths):
        # print('explode')
        return reduce(*explode(vals, depths))
    elif any(v >= 10 for v in vals):
        # print('split')
        return reduce(*split(vals, depths))
    else:
        return vals, depths


def add(number_1, number_2):
    v1, d1 = number_1
    v2, d2 = number_2

    return v1 + v2, [d + 1 for d in d1] + [d +1 for d in d2]


def magnitude(vals, depths):
    d_prev = -1
    for ix, (v, d) in enumerate(zip(vals, depths)):
        if d == d_prev:
            mag = 3*vals[ix-1] + 2*vals[ix]
            new_depth = d-1
            mag_ix = ix
            break

        d_prev = d

    vals[mag_ix-1] = mag
    depths[mag_ix-1] = new_depth
    del vals[mag_ix]
    del depths[mag_ix]

    if depths == [-1]:
        return vals
    else:
        return magnitude(vals, depths)


max_mag = 0
for ix in range(len(char_sequences)):
    for iy in range(len(char_sequences)):
        [mag] = magnitude(*reduce(*add(parse_number(char_sequences[ix]), parse_number(char_sequences[iy]))))
        max_mag = max(max_mag, mag)
        [mag] = magnitude(*reduce(*add(parse_number(char_sequences[iy]), parse_number(char_sequences[ix]))))
        max_mag = max(max_mag, mag)

print(max_mag)
