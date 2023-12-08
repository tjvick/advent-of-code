from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

seeds = []
conversion_directions = {}
mapping_conversions = {}
ranges = []
source_category = None

for line in strings:
    first_line_match = re.match(r'seeds: (.*)', line)
    if first_line_match:
        seeds = [int(x) for x in first_line_match.group(1).split()]

    map_match = re.match(r'(.+)-to-(.+) map(.*)', line)
    if map_match:
        if source_category is not None:
            mapping_conversions[source_category] = ranges

        ranges = []
        source_category = map_match.group(1)
        destination_category = map_match.group(2)
        conversion_directions[source_category] = destination_category

    mapping_match = re.match(r'(\d+) (\d+) (\d+)', line)
    if mapping_match:
        mapping_values = [int(x) for x in mapping_match.groups()]
        dest_start_index, source_start_index, length = mapping_values
        destination_range = (dest_start_index, dest_start_index + length)
        source_range = (source_start_index, source_start_index + length)
        ranges.append([source_range, dest_start_index-source_start_index])

mapping_conversions[source_category] = ranges

print(conversion_directions)
print(mapping_conversions)

current_category = 'seed'
final_category = 'location'
locations = []
for seed in seeds:
    current_value = seed
    current_category = 'seed'

    while current_category != final_category:
        amount_to_add = 0
        for mapping_conversion in mapping_conversions[current_category]:
            source_range, delta = mapping_conversion
            if source_range[0] <= current_value < source_range[1]:
                amount_to_add = delta
                break

        new_value = current_value + amount_to_add

        current_value = new_value
        current_category = conversion_directions[current_category]

    locations.append(current_value)

print(locations)
print(min(locations))
