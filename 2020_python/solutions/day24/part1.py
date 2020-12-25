import numpy as np
import re
from collections import defaultdict

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]


def get_all_directions(file_contents):
    all_directions = []
    for row_contents in file_contents:
        directions = []
        row = row_contents

        def _sub(match):
            directions.append(match.group(0))
            return ''

        while len(row) > 0:
            row = re.sub(r'^(n|s)?e|(n|s)?w', _sub, row)

        all_directions.append(directions)

    return all_directions


movements = {
    'e': np.array((2, 0)),
    'w': np.array((-2, 0)),
    'ne': np.array((1, 1)),
    'nw': np.array((-1, 1)),
    'se': np.array((1, -1)),
    'sw': np.array((-1, -1))
}

tiles = defaultdict(bool)

directions_set = get_all_directions(file_contents)
for directions in directions_set:
    location = np.array((0, 0))
    for direction in directions:
        location += movements[direction]

    tiles[tuple(location)] = not tiles[tuple(location)]


n_flipped = sum(tiles.values())
print(n_flipped)

