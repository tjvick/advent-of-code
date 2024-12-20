from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

input_lines = helpers.read_each_line_as_string(filepath)

available_towels = input_lines[0].split(', ')

desired_designs = input_lines[2:]

def design_can_be_constructed(design):
    remaining_designs = [design]
    while remaining_designs:
        remaining_design = remaining_designs.pop()
        for towel in available_towels:
            if remaining_design == towel:
                return True
            if remaining_design.startswith(towel):
                remaining_designs.append(remaining_design[len(towel):])

    return False


n_possible_designs = 0
for desired_design in desired_designs:
    can_be_constructed = design_can_be_constructed(desired_design)
    n_possible_designs += int(can_be_constructed)
    # print(desired_design, can_be_constructed)

print(n_possible_designs)



