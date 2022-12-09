from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

RIGHT = "R"
LEFT = "L"
DOWN = "D"
UP = "U"

H = np.array([0, 0])
T = np.array([0, 0])


def follow(H, T):
    if max(abs(H - T)) > 1:
        T += (np.sign(H - T))


T_positions = set()
for string in strings:
    [direction, distance] = string.split()
    distance = int(distance)

    for ix in range(distance):
        if direction == RIGHT:
            H += [1, 0]
        elif direction == LEFT:
            H += [-1, 0]
        elif direction == UP:
            H += [0, 1]
        elif direction == DOWN:
            H += [0, -1]
        follow(H, T)
        T_positions.add(tuple(T))

print(len(T_positions))