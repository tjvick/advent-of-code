from solutions import helpers
import numpy as np

filename = 'input'

int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename, delimiter=",")
positions = int_sequences[0]

target = np.median(positions)
fuel_requied = sum(np.abs(positions - target))

print(fuel_requied)



