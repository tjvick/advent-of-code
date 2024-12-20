from functools import lru_cache

from solutions import helpers

filepath = 'input'
# filepath = 'test'

input_lines = helpers.read_each_line_as_string(filepath)

available_towels = input_lines[0].split(', ')

desired_designs = input_lines[2:]

@lru_cache
def count_possible_towel_arrangements(remaining_design):
    total_count_for_this_remaining_design = 0
    for towel in available_towels:
        if remaining_design == towel:
            total_count_for_this_remaining_design += 1
        elif remaining_design.startswith(towel):
            total_count_for_this_remaining_design += count_possible_towel_arrangements(remaining_design[len(towel):])

    return total_count_for_this_remaining_design


n_possible_designs = 0
for desired_design in desired_designs:
    count_for_this_design = count_possible_towel_arrangements(desired_design)
    n_possible_designs += count_for_this_design

print(n_possible_designs)



