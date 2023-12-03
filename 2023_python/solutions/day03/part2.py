from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

all_numbers = []

for ix_line, line in enumerate(strings):
    found_numbers = re.finditer('(\d+)', line)
    if found_numbers:
        for found_number in found_numbers:
            adjacent_locations = []
            a = found_number.start()
            b = found_number.end()

            for irow in range(ix_line-1, ix_line+2):
                print(irow)
                for icol in range(a-1, b+1):
                    adjacent_locations.append((irow, icol))

            print(found_number.group(), adjacent_locations)
            all_numbers.append((int(found_number.group()), adjacent_locations))

all_symbols = []

for ix_line, line in enumerate(strings):
    found_symbols = re.finditer(r'[^.0-9]', line)
    if found_symbols:
        for found_symbol in found_symbols:
            found_symbol.start()
            all_symbols.append((found_symbol.group(), (ix_line, found_symbol.start())))

print(all_numbers)
print(all_symbols)

engine_part_numbers = []
non_part_numbers = []
possible_gears = {}

for number in all_numbers:
    number_value = number[0]
    eligible_locations = number[1]

    found = False
    for symbol in all_symbols:
        if symbol[1] in eligible_locations:
            if symbol[0] == '*':
                if symbol[1] not in possible_gears:
                    possible_gears[symbol[1]] = [number_value]
                else:
                    possible_gears[symbol[1]].append(number_value)


    if found:
        engine_part_numbers.append(number_value)
    else:
        non_part_numbers.append(number_value)

print(possible_gears)

gear_ratio_sum = 0

for possible_gear_location, possible_gear_numbers in possible_gears.items():
    if len(possible_gear_numbers) == 2:
        gear_ratio = possible_gear_numbers[0] * possible_gear_numbers[1]
        gear_ratio_sum += gear_ratio

print(gear_ratio_sum)
