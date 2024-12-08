from collections import defaultdict

from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

data = helpers.read_as_2d_array_of_characters(filepath)

starting_location = np.argwhere(data == '^')[0]

next_direction = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1)
}

def get_all_path_locations(data):
    location = (int(starting_location[0]), int(starting_location[1]))
    direction = (-1, 0)

    visited_locations = set()
    visited_locations.add(location)

    while True:
        new_location = (location[0] + direction[0], location[1] + direction[1])

        if new_location[0] < 0 or new_location[0] >= data.shape[0]:
            break
        if new_location[1] < 0 or new_location[1] >= data.shape[1]:
            break

        if data[new_location[0], new_location[1]] == '#':
            direction = next_direction[direction]
        else:
            location = new_location

        visited_locations.add(location)

    return visited_locations


def has_looping_path(data):
    location = (int(starting_location[0]), int(starting_location[1]))
    direction = (-1, 0)

    location_directions = defaultdict(list)
    location_directions[location].append(direction)

    while True:
        proposed_new_location = (location[0] + direction[0], location[1] + direction[1])

        if proposed_new_location[0] < 0 or proposed_new_location[0] >= data.shape[0]:
            return False
        if proposed_new_location[1] < 0 or proposed_new_location[1] >= data.shape[1]:
            return False

        if data[proposed_new_location[0], proposed_new_location[1]] == '#':
            # turn right
            direction = next_direction[direction]
        elif direction in location_directions[proposed_new_location]:
            # we've been to the new location already
            return True
        else:
            location = proposed_new_location

        location_directions[location].append(direction)


obstacle_count = 0

path_locations = get_all_path_locations(data)

print(path_locations)

for path_location in path_locations:
    new_map = np.copy(data)
    new_map[path_location[0], path_location[1]] = '#'
    has_loop = has_looping_path(new_map)
    if has_loop:
        obstacle_count += 1
        print('Obstacle!', path_location)

print(obstacle_count)

# 5154 too high
# 1913 too high
# 1831 too high