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

def oxygen_rating(report):
    remainder = report.copy()
    for ix in range(0, np.shape(report)[1]):
        column = remainder[:, ix]
        most_common = mode(column)
        if (sum(column == most_common) == len(column) / 2):
            most_common = 1
        print(column == most_common)
        remainder = remainder[column == most_common, :]
        if np.shape(remainder)[0] == 1:
            rating_bits = "".join(str(x) for x in remainder[0, :])
            print(rating_bits)
            rating = int("".join(str(x) for x in remainder[0, :]), 2)

            print(rating)
            return rating


def co2_rating(report):
    remainder = report.copy()
    for ix in range(0, np.shape(report)[1]):
        column = remainder[:, ix]
        least_common = 1 - mode(column)
        if (sum(column == least_common) == len(column) / 2):
            least_common = 0
        print(column == least_common)
        remainder = remainder[column == least_common, :]
        if np.shape(remainder)[0] == 1:
            rating_bits = "".join(str(x) for x in remainder[0, :])
            print(rating_bits)
            rating = int("".join(str(x) for x in remainder[0, :]), 2)

            print(rating)
            return rating


oxy = oxygen_rating(report)
co2 = co2_rating(report)
print(oxy, co2, oxy*co2)


