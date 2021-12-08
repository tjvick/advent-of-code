from solutions import helpers
import numpy as np

filename = 'input'

int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename, delimiter=",")
positions = int_sequences[0]

min_fuel_required = 1e24
for target in range(0, max(positions)):
    fuel_required = sum(map(lambda n: n * (n+1) / 2, np.abs(positions - target)))
    if fuel_required < min_fuel_required:
        min_fuel_required = fuel_required

print(min_fuel_required)