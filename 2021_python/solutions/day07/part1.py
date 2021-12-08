from solutions import helpers
import numpy as np

filename = 'input'

int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename, delimiter=",")
positions = int_sequences[0]

min_fuel_required = sum(np.abs(positions - np.median(positions)))

print(min_fuel_required)



