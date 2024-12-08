from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

data = helpers.read_as_2d_array_of_characters(filepath)

starting_location = np.argwhere(data == '^')[0]
print(starting_location)
# print(data[*starting_location])

next_direction = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1)
}

direction = (-1, 0)
location = (int(starting_location[0]), int(starting_location[1]))
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

    print(location)

    visited_locations.add(location)

print(visited_locations)
print(len(visited_locations))
