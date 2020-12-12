import re
import numpy as np

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

directions = {
    'E': 0,
    'N': 90,
    'W': 180,
    'S': 270
}

rotation_direction = {
    'R': -1,
    'L': 1
}

unit_velocities = {
    0: [1, 0],
    90: [0, 1],
    180: [-1, 0],
    270: [0, -1]
}


def rotate(pos, angle):
    M = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]]
    ).astype(int)
    return np.dot(M, np.transpose(pos))


pos = np.array([0, 0])
wp_pos = np.array([10, 1])

for movement in file_contents:
    match = re.match(r'^([A-Z])(\d+)$', movement)
    letter = match.group(1)
    number = int(match.group(2))

    if letter == 'F':
        pos += wp_pos * number

    if letter in 'NSEW':
        wp_pos += np.array(unit_velocities[directions[letter]]) * number

    if letter in 'RL':
        wp_pos = rotate(wp_pos, rotation_direction[letter] * np.deg2rad(number))

print(abs(pos[0]) + abs(pos[1]))
