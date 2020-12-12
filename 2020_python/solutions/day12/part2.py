import re
import numpy as np

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]


rotation_direction = {
    'R': -1,
    'L': 1
}

unit_velocities = {
    0: [1, 0],
    90: [0, 1],
    180: [-1, 0],
    270: [0, -1],
    'E': [1, 0],
    'N': [0, 1],
    'W': [-1, 0],
    'S': [0, -1]
}

M = np.array([[0, -1], [1, 0]])


def rotate90(vector, k):
    for ix in range(int(k % 4)):
        vector = np.dot(M, vector)
    return vector


pos = np.array([0, 0])
wp_pos = np.array([10, 1])

for movement in file_contents:
    match = re.match(r'^([A-Z])(\d+)$', movement)
    letter = match.group(1)
    number = int(match.group(2))

    if letter == 'F':
        pos += wp_pos * number

    if letter in 'NSEW':
        wp_pos += np.array(unit_velocities[letter]) * number

    if letter in 'RL':
        angle = rotation_direction[letter] * number
        wp_pos = rotate90(wp_pos, angle / 90)

print(sum(abs(pos)))
