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

time_line = strings[0]
dist_line = strings[1]

tm = re.match(r'Time:(.+)', time_line)
dm = re.match(r'Distance:(.+)', dist_line)

times = tm.group(1).strip().split()
print(times)
distances = dm.group(1).strip().split()
print(distances)

margin_of_error = 1
for total_race_time, record_distance in zip(times, distances):
    a = 1
    b = int(total_race_time) * -1
    c = int(record_distance)+0.01
    min_charge_time_for_record = (-b - (b**2 - 4 * a * c)**(1/2))/(2*a)
    max_charge_time_for_record = (-b + (b**2 - 4 * a * c)**(1/2))/(2*a)

    print(min_charge_time_for_record, max_charge_time_for_record)
    min_charge_time_ms = np.ceil(min_charge_time_for_record)
    max_charge_time_ms = np.floor(max_charge_time_for_record)
    print(min_charge_time_ms, max_charge_time_ms)

    n_ways_to_win = max_charge_time_ms - min_charge_time_ms + 1
    print(n_ways_to_win)

    margin_of_error *= n_ways_to_win

print(margin_of_error)
