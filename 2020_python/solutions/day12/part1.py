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

yaw = 0
pos = np.array([0, 0])

for movement in file_contents:
    match = re.match(r'^([A-Z])(\d+)$', movement)
    letter = match.group(1)
    number = int(match.group(2))

    if letter == 'F':
        pos += np.array(unit_velocities[yaw]) * number

    if letter in 'NSEW':
        pos += np.array(unit_velocities[directions[letter]]) * number

    if letter in 'RL':
        yaw = (yaw + rotation_direction[letter] * number) % 360


print(abs(pos[0]) + abs(pos[1]))
