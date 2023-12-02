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

map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

sum = 0
for calibration_line in strings:
    earliest_index = 1000
    earliest_digit = ""
    for key, value in map.items():
        index = re.search(key, calibration_line)
        if index:
            if index.span()[0] < earliest_index:
                earliest_index = index.span(0)[0]
                earliest_digit = value

    latest_index = -1
    latest_digit = ""
    for key, value in map.items():
        index = re.finditer(key, calibration_line)
        if index:
            for m in index:
                if m.start() > latest_index:
                    latest_index = m.start(0)
                    latest_digit = value

    calibration_value_string = earliest_digit + latest_digit
    calibration_value_int = int(calibration_value_string)
    print(calibration_line, calibration_value_int)
    sum += calibration_value_int

print(sum)

# not 53869
# not 53889
# is 53866
