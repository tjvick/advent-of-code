from solutions import helpers as h
import numpy as np
from scipy import stats

filename = 'input'

digit_sequences = h.read_each_line_as_digit_sequence(filename)

report = np.array(digit_sequences)


def keep_numbers_matching_mode(filtered_report, ix, anti=False):
    if len(filtered_report) == 1:
        return filtered_report

    column = filtered_report[:, ix]
    [most_common, n_occurrences] = stats.mode(column)
    if n_occurrences == len(column) / 2:
        most_common = 1
    value_to_keep = most_common if not anti else 1 - most_common
    return keep_numbers_matching_mode(filtered_report[column == value_to_keep], ix + 1, anti)


def oxygen_generator_rating(filtered_report):
    rating_bits = keep_numbers_matching_mode(filtered_report, 0)[0]
    return h.bit_sequence_to_int(rating_bits)


def co2_scrubber_rating(filtered_report):
    rating_bits = keep_numbers_matching_mode(filtered_report, 0, anti=True)[0]
    return h.bit_sequence_to_int(rating_bits)


oxy = oxygen_generator_rating(report)
co2 = co2_scrubber_rating(report)
print(oxy, co2, oxy*co2)


