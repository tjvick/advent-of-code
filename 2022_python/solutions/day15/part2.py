from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

boundary = 4000000
# boundary = 20

strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)


def distance(a, b):
    return sum(abs(a-b))


def within_bounds(possible_location):
    return (0 < possible_location[0] < boundary) and (0 < possible_location[1] < boundary)


borders = set()
sensors = []
beacons = set()
for string in strings:
    m = re.match(r'^Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)$', string)
    print(m.groups())
    sensor_x, sensor_y, beacon_x, beacon_y = m.groups()
    sensor = np.array([int(sensor_x), int(sensor_y)])
    beacon = np.array([int(beacon_x), int(beacon_y)])

    beacons.add(tuple(beacon))

    d = sum(abs(sensor - beacon))

    sensors.append([tuple(sensor), d])

    x_0 = sensor[0]
    x_min = sensor[0] - d - 1
    x_max = sensor[0] + d + 1
    y_0 = sensor[1]
    y_min = sensor[1] - d - 1
    y_max = sensor[1] + d + 1

    # sensor_borders = []
    for x, y in zip(range(x_max, x_0, -1), range(y_0, y_min, -1)):
        if within_bounds((x, y)):
            borders.add((x, y))
        # sensor_borders.append((x,y))

    for x, y in zip(range(x_0, x_min, -1), range(y_min, y_0, 1)):
        if within_bounds((x, y)):
            borders.add((x, y))
        # sensor_borders.append((x, y))

    for x, y in zip(range(x_min, x_0, 1), range(y_0, y_max, 1)):
        if within_bounds((x, y)):
            borders.add((x, y))
        # sensor_borders.append((x, y))

    for x, y in zip(range(x_0, x_max, 1), range(y_max, y_0, -1)):
        if within_bounds((x, y)):
            borders.add((x, y))
        # sensor_borders.append((x, y))

    # print(sensor_borders)

print(len(borders))
possible_distress_locations = borders


def in_any_sensor_range(location):
    for sensor_loc, sensor_d in sensors:
        if distance(location, sensor_loc) <= sensor_d:
            return True

    return False


tuning_freq = None
counter = 0
for possible_location in possible_distress_locations:
    counter += 1
    if counter % 100000 == 0:
        print(counter)
    # if (0 < possible_location[0] < boundary) and (0 < possible_location[1] < boundary):
    if not in_any_sensor_range(np.array(possible_location)):
        print(possible_location)
        x, y = possible_location
        tuning_freq = x*4000000 + y
        print(tuning_freq)

print(tuning_freq)

# sensor_grid = np.zeros((40, 40), dtype=int)
# for loc in borders:
#     sensor_grid[loc] = 1
#
# for row in sensor_grid:
#     print(row)
