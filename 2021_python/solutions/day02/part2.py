from solutions import helpers
import numpy as np

filename = 'input'

strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
# digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

x = 0
aim = 0
y = 0
for instruction in strings:
    (direction, amt) = instruction.split()
    match direction:
        case "forward":
            y += int(amt) * aim
            x += int(amt)
        case "down":
            aim += int(amt)
        case "up":
            aim -= int(amt)


print(x, y)
print(x*y)


