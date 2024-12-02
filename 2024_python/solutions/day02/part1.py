from solutions import helpers
import numpy as np

filepath = 'input'

reports = helpers.read_as_list_of_delimited_arrays(filepath, delimiter=' ', dtype=int)


def is_safe(report):
    diff = report[1:] - report[:-1]
    is_monotonic = abs(sum(np.sign(diff))) == len(diff)
    differs_by_at_least_one = min(abs(diff)) >= 1
    differs_by_at_most_three = max(abs(diff)) <= 3

    return is_monotonic and differs_by_at_least_one and differs_by_at_most_three


n_safe_reports = sum(is_safe(report) for report in reports)

print(n_safe_reports)
