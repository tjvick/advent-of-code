from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

target_row = 2000000
# target_row = 10

strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

def distance(a, b):
    return sum(abs(a-b))

ineligible_x_ranges = []
ineligible_locations = set()
beacons = set()
for string in strings:
    m = re.match(r'^Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)$', string)
    print(m.groups())
    sensor_x, sensor_y, beacon_x, beacon_y = m.groups()
    sensor = np.array([int(sensor_x), int(sensor_y)])
    beacon = np.array([int(beacon_x), int(beacon_y)])
    beacons.add(tuple(beacon))

    d = sum(abs(sensor-beacon))

    min_x = min(sensor[0], beacon[0]) - d
    max_x = max(sensor[0], beacon[0]) + d

    for x in range(min_x, max_x):
        y = target_row
        location = np.array([x, y])
        if distance(sensor, location) <= d:
            ineligible_locations.add(tuple(location))

ineligible_locations.difference_update(beacons)
print(ineligible_locations)
print(len(ineligible_locations))

print(sorted([x for x, y in ineligible_locations]))


