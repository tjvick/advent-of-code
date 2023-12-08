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

left_right_instructions = [x for x in strings[0]]

element_map = {}
for line in strings[2:]:
    m = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
    current, left, right = m.groups()
    element_map[current] = (left, right)

current_element = "AAA"
final_element = "ZZZ"

n_steps = 0

while True:
    print(current_element, element_map[current_element])
    instruction = left_right_instructions.pop(0)
    print('instruction', instruction)
    left_element, right_element = element_map[current_element]
    if instruction == "L":
        current_element = left_element
    else:
        current_element = right_element

    print('new current_element', current_element)
    n_steps += 1

    if current_element == final_element:
        break

    left_right_instructions.append(instruction)

print(n_steps)
