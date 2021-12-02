from solutions import helpers
import numpy as np

filename = 'input'

[values] = helpers.read_as_digit_list(filename)

sequence = np.append(values, values[0])

print(len(values))
print(len(sequence))

print(sum((sequence[1:] == sequence[0:-1]) * sequence[0:-1]))

