from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

grid_size = (70, 70)
# grid_size = (6, 6)

n_bytes_to_fall = 1024
# n_bytes_to_fall = 12

byte_positions = helpers.read_as_2d_array_of_delimited_values(filepath, delimiter=',', dtype=int)

starting_location = (0, 0)
ending_location = grid_size

def inbounds(location):
    return 0 <= location[0] <= grid_size[0] and 0 <= location[1] <= grid_size[1]

def neighbors(location):
    x, y = location
    possible_next_steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(x + dx, y + dy) for (dx, dy) in possible_next_steps if inbounds((x + dx, y + dy))]


def find_path(corrupted):
    paths = [(starting_location, 1)]
    fewest_steps_to_location = {}

    shortest_path_length = np.inf
    while paths:
        path = paths.pop(0)
        last_location = path[0]
        path_length = path[1]

        if path_length >= shortest_path_length:
            continue

        if last_location in fewest_steps_to_location:
            if path_length >= fewest_steps_to_location[last_location]:
                continue

        fewest_steps_to_location[last_location] = path_length

        possible_neighbors = neighbors(last_location)
        for possible_neighbor in possible_neighbors:
            if possible_neighbor in fewest_steps_to_location and fewest_steps_to_location[possible_neighbor] <= path_length + 1:
                continue
            if possible_neighbor in corrupted:
                continue
            if possible_neighbor == ending_location:
                if len(path) + 1 < shortest_path_length:
                    # print("New shortest path of length", path_length + 1)
                    shortest_path_length = path_length + 1
            else:
                paths.append((possible_neighbor, path_length + 1))

    return shortest_path_length - 1


corrupted_locations = set()

for byte_position in byte_positions[:1024]:
    corrupted_locations.add(tuple(int(_) for _ in byte_position))


for byte_position in byte_positions[1024:]:
    print(byte_position)
    corrupted_locations.add(tuple(int(_) for _ in byte_position))

    shortest_path = find_path(corrupted_locations)
    print(shortest_path)

    if shortest_path == np.inf:
        print(byte_position)
        break
