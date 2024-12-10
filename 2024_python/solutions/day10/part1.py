from collections import defaultdict

from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

topographic_map = helpers.read_as_2d_array_of_characters(filepath, dtype=int)

trailhead_locations = np.argwhere(topographic_map == 0)

paths = [[loc,] for loc in trailhead_locations]

directions = [np.array(x) for x in [(1, 0), (-1, 0), (0, 1), (0, -1)]]

full_hiking_paths = []

def inbounds(idx_row, idx_col):
    if (
        0 <= idx_row < topographic_map.shape[0] and
        0 <= idx_col < topographic_map.shape[1]
    ):
        return True

while len(paths) > 0:
    current_path = paths.pop()
    last_known_location = current_path[-1]
    last_known_height = topographic_map[*last_known_location]

    for direction in directions:
        possible_next_location = last_known_location + direction
        if not inbounds(*possible_next_location):
            continue

        possible_next_height = topographic_map[*possible_next_location]
        if possible_next_height == last_known_height + 1:
            new_path = current_path + [possible_next_location]
            if possible_next_height == 9:
                full_hiking_paths.append(new_path)
            else:
                paths.append(new_path)

print(len(full_hiking_paths)) # this is part 2 answer

hiking_path_endpoints = defaultdict(set)
for full_hiking_path in full_hiking_paths:
    a = tuple(full_hiking_path[0])
    b = tuple(full_hiking_path[-1])
    hiking_path_endpoints[a].add(b)

trail_scores = {trailhead: len(hiking_path_endpoints[trailhead]) for trailhead in hiking_path_endpoints}

total_trail_score = sum(trail_scores.values())

print(total_trail_score) # this is part 1 answer