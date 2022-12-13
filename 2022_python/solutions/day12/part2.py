from solutions import helpers
import numpy as np
import re
import random

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

# strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

char_array = np.matrix(char_sequences, dtype='str')
start_location = np.where(char_array == "S")
start_location = start_location[0][0], start_location[1][0]
end_location = np.where(char_array == "E")
end_location = end_location[0][0], end_location[1][0]

heatmap_ints = []
for char_sequence in char_sequences:
    heatmap_ints.append([0 if x == "S" else 25 if x == "E" else ord(x) - ord('a') for x in char_sequence])

heatmap = np.array(heatmap_ints, dtype=int)

print(heatmap)
print(start_location)
print(end_location)

all_paths = [([end_location], 25)]
min_distance = 10000  # heatmap.size
bounds = heatmap.shape
min_elevation_so_far = 26
shortest_paths = {}
shortest_distance_to_elevation = {}
visited = set()
min_path = []

counter = 0
while all_paths:
    # if (20, )

    counter += 1
    # if counter > 100:
    #     break

    elevations = [el for path, el in all_paths]
    if min(elevations) < min_elevation_so_far:
        min_elevation_so_far = min(elevations)
        shortest_distance_to_elevation[min_elevation_so_far] = 1000
        print("min_elevation_so_far", min_elevation_so_far, len(all_paths))
    # ix_options = np.argwhere([el <= min(elevations) + 4 for el in elevations])
    # if len(ix_options):
    #     # ix = np.argmin(elevations)
    #     ix = random.choice(ix_options)[0]
    # else:
    #     ix = len(all_paths)-1

    # ix = 0
    # print(ix_options)
    # print(ix)

    path, el = all_paths.pop(0)
    # if len(path) > min_distance:
        # continue

    if shortest_distance_to_elevation[el] > len(path):
        shortest_distance_to_elevation[el] = len(path)
        print(shortest_distance_to_elevation)

    location = path[len(path)-1]
    # print(location, heatmap[location])
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_location = tuple(np.array(location) + direction)
        # if new_location not in visited:
        # if new_location not in path:
        if new_location[0] in range(bounds[0]) and new_location[1] in range(bounds[1]):
            if heatmap[location] - heatmap[new_location] <= 1:
                if new_location == start_location:
                    if len(path) < min_distance:
                        min_path = path
                    min_distance = min(len(path), min_distance)
                    print(min_distance, len(all_paths), counter, path)
                if new_location not in shortest_paths or shortest_paths[new_location] > len(path)+1:
                    shortest_paths[new_location] = len(path)+1
                    all_paths.append((path + [new_location], heatmap[new_location]))
                    visited.add(new_location)

print("min_distance", min_distance)
print("counter", counter)
print("len(visited)", len(visited))
print("size", heatmap.size)
print("min_path", min_path)

path_map = np.zeros_like(heatmap)
for item in min_path:
    path_map[item] = 1
# for row in path_map:
#     print(''.join([str(x) for x in row]))

print([heatmap[item] for item in min_path])

visitation_map = np.zeros_like(heatmap)
for item in visited:
    visitation_map[item] = 1
# for row in visitation_map:
#     print(''.join([str(x) for x in row]))

print(shortest_paths)
print(shortest_distance_to_elevation)
# print(shortest_paths[(20, 0)])