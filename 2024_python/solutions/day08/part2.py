import math
from itertools import combinations

from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

input_map = helpers.read_as_2d_array_of_characters(filepath)

unique_characters = set(input_map.flatten()).difference('.')

antinodes = list()

def get_smallest_mappable_step_between_antennas(antenna_pair):
    a, b = antenna_pair
    delta = b - a

    dy, dx = delta
    gcd = math.gcd(dy, dx)
    return np.array([ int(dy / gcd), int(dx / gcd) ])


def within_range(location) -> bool:
    ix_row, ix_col = location
    return (
            0 <= ix_row < input_map.shape[0] and
            0 <= ix_col < input_map.shape[1]
    )


for unique_character in unique_characters:
    antenna_locations = np.argwhere(input_map == unique_character)
    print(unique_character)

    antenna_pairs = list(combinations(antenna_locations, 2))

    for antenna_pair in antenna_pairs:
        a, b = antenna_pair
        delta = get_smallest_mappable_step_between_antennas(antenna_pair)

        loc = a.copy()
        while within_range(loc):
            antinodes.append(loc + delta)
            loc += delta

        loc = b.copy()
        while within_range(loc):
            antinodes.append(loc - delta)
            loc -= delta


unique_antinodes = set(tuple(map(int,antinode)) for antinode in antinodes)
unique_antinodes_within_range = [ua for ua in unique_antinodes if within_range(ua)]

print(len(unique_antinodes_within_range))