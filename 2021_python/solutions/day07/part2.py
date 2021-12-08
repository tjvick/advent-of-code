from solutions import helpers
import numpy as np

filename = 'input'

int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename, delimiter=",")
positions = int_sequences[0]


f_x = lambda target: sum(map(lambda n: n * (n+1) / 2, np.abs(positions - target)))
print(np.mean(positions))
min_fuel_required = helpers.find_local_minimum(f_x, int(np.mean(positions)), min(positions), max(positions))

print(min_fuel_required)
