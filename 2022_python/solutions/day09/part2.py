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

n_knots = 10
knots = []
for ix in range(n_knots):
    knots.append(np.array([0, 0]))


def follow(H, T):
    if max(abs(H - T)) > 1:
        T += (np.sign(H - T))


tail_positions = set()
for string in strings:
    [direction, distance] = string.split()
    distance = int(distance)

    for ix in range(distance):
        if direction == RIGHT:
            knots[0] += [1, 0]
        elif direction == LEFT:
            knots[0] += [-1, 0]
        elif direction == UP:
            knots[0] += [0, 1]
        elif direction == DOWN:
            knots[0] += [0, -1]
        for ik in range(1, n_knots):
            follow(knots[ik-1], knots[ik])
        tail_positions.add(tuple(knots[n_knots-1]))

print(len(tail_positions))