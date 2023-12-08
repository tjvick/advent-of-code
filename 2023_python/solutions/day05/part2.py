from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

def get_overlap(mapping_range, current_range):
    a, b = current_range
    c, d = mapping_range

    if b < c or a > d:
        return None
    else:
        overlap = (max(a, c), min(b, d))
        return overlap

strings = helpers.read_each_line_as_string(filename)

seeds = []
seed_ranges = []

conversion_directions = {}
mapping_conversions = {}
ranges = []
source_category = None


for line in strings:
    first_line_match = re.match(r'seeds: (.*)', line)
    if first_line_match:
        seeds = [int(x) for x in first_line_match.group(1).split()]
        for ix in range(int(len(seeds) / 2)):
            seed_ranges.append((seeds[ix*2], seeds[ix*2]+seeds[ix*2+1]-1))

    map_match = re.match(r'(.+)-to-(.+) map(.*)', line)
    if map_match:
        if source_category is not None:
            if min(x[0][0] for x in ranges) > 0:
                ranges.append(((0, min(x[0][0] for x in ranges)), 0))
            ranges.append(((max(x[0][1] for x in ranges), 1e16), 0))
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


if min(x[0][0] for x in ranges) > 0:
    ranges.append(((0, min(x[0][0] for x in ranges)), 0))
ranges.append(((max(x[0][1] for x in ranges), 1e16), 0))
mapping_conversions[source_category] = ranges

print(conversion_directions)
print(mapping_conversions)

current_category = 'seed'
final_category = 'location'
locations = []
final_locations = set()

for seed_range in seed_ranges:
    current_ranges = set([seed_range])
    current_category = 'seed'

    while current_category != final_category:
        print('\n', current_category)
        new_ranges = set()
        while current_ranges:
            current_range = current_ranges.pop()
            print('current range:', current_range)
            remaining_range = current_range
            bottom_covered = False
            top_covered = False
            all_min_values_for_source_ranges = []
            for mapping_conversion in mapping_conversions[current_category]:
                source_range, delta = mapping_conversion
                print('source range: ', source_range)
                overlap = get_overlap(source_range, current_range)
                if overlap is not None:
                    destination_range = overlap[0] + delta, overlap[1] + delta
                    print('destination_range:', destination_range)
                    new_ranges.add(destination_range)
                    # might still have more mapping to do
                # current_ranges.update(remaining)

        current_ranges = new_ranges
        current_category = conversion_directions[current_category]
        print(current_category)
        print(current_ranges)

    final_locations.update(current_ranges)

print(min(x[0] for x in final_locations))

# 58234309 too high
# 15290096 just right
