from solutions import helpers
import numpy as np
from statistics import mode


filename = 'input'

# strings = helpers.read_each_line_as_string(filename)
# ints = helpers.read_each_line_as_int(filename)
# floats = helpers.read_each_line_as_float(filename)
# char_sequences = helpers.read_each_line_as_char_sequence(filename)
digit_sequences = helpers.read_each_line_as_digit_sequence(filename)
# int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename)

report = np.array(digit_sequences)

modes = []
for ix in range(0, np.shape(report)[1]):
    column = report[:, ix]
    modes.append(mode(column))

gamma_bits = "".join(str(x) for x in modes)

epsilon_bits = "".join(str(1-x) for x in modes)

gamma = int(gamma_bits, 2)
epsilon = int(epsilon_bits, 2)
print(gamma, epsilon, gamma*epsilon)



