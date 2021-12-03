from solutions import helpers as h
import numpy as np
from scipy import stats

filename = 'input'

digit_sequences = h.read_each_line_as_digit_sequence(filename)

report = np.array(digit_sequences)

[modes, _] = stats.mode(report, axis=0)

gamma_rate = h.bit_sequence_to_int(modes[0])
epsilon_rate = h.bit_sequence_to_int(1 - modes[0])

print(gamma_rate, epsilon_rate, gamma_rate * epsilon_rate)
