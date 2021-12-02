from solutions import helpers
import numpy as np

filename = 'input'

[values] = helpers.read_as_digit_list(filename)

half = int(len(values) / 2)

sequence = np.concatenate((values, values[0:half]))

answer = sum((sequence[half:] == sequence[0:-half]) * sequence[0:-half])

print(answer)

