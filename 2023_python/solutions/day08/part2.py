from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

left_right_instructions_og = [x for x in strings[0]]

element_map = {}
for line in strings[2:]:
    m = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
    current, left, right = m.groups()
    element_map[current] = (left, right)

elements_that_end_in_A = [el for el in element_map if el.endswith('A')]


current_elements = elements_that_end_in_A
n_steps = 0
n_steps_between = []

for starting_element in elements_that_end_in_A:
    print('starting element', starting_element)

    left_right_instructions = left_right_instructions_og.copy()

    current_element = starting_element
    n_steps = 0

    while True:
        instruction = left_right_instructions.pop(0)
        left_element, right_element = element_map[current_element]
        if instruction == "L":
            current_element = left_element
        else:
            current_element = right_element

        n_steps += 1

        if current_element.endswith('Z'):
            n_steps_between.append(n_steps)
            break

        left_right_instructions.append(instruction)

print("n steps between", n_steps_between)
lcm = np.lcm.reduce(n_steps_between)
print("lcm", lcm)
