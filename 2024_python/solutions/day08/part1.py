from itertools import combinations

from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

input_map = helpers.read_as_2d_array_of_characters(filepath)

unique_characters = set(input_map.flatten()).difference('.')

# print(input_map)
print(unique_characters)

antinodes = list()

for unique_character in unique_characters:
    antenna_locations = np.argwhere(input_map == unique_character)
    print(unique_character)
    # print(antenna_locations)

    antenna_pairs = list(combinations(antenna_locations, 2))
    # print(antenna_pairs)

    for antenna_pair in antenna_pairs:
        a, b = antenna_pair
        delta = b - a
        antinode_1 = b + delta
        antinode_2 = a - delta

        antinodes.extend([antinode_1, antinode_2])

    '''
    a, b
    b + b - a = 2b - a
    a - b + a = 2a - b
    '''

def within_range(location) -> bool:
    ix_row, ix_col = location
    return (
            0 <= ix_row < input_map.shape[0] and
            0 <= ix_col < input_map.shape[1]
    )

# print(antinodes)
unique_antinodes = set(tuple(map(int,antinode)) for antinode in antinodes)
unique_antinodes_within_range = [ua for ua in unique_antinodes if within_range(ua)]

# print(unique_antinodes_within_range)
print(len(unique_antinodes_within_range))