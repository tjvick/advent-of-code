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


def is_safe_with_removed_level(report):
    if is_safe(report):
        return True

    for ix in range(len(report)):
        shortened_report = np.delete(report, ix)
        if is_safe(shortened_report):
            return True

    return False


n_safe_reports = sum(is_safe_with_removed_level(report) for report in reports)

print(n_safe_reports)
