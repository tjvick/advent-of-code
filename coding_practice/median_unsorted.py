import numpy as np
import time

input_array = [1, 5, 2, 2, 4, 8, 5, 4, 9, 2]
# sorted = [1, 2, 2, 2,   4, 4,    5, 5, 8, 9]

def median_supereasy(x):
    return np.median(x)


def median_easy(x):
    sorted_input = sorted(x)
    if len(x) % 2 > 0:
        middle = int((len(x) - 1) / 2)
        return sorted_input[middle]

    middle = int(len(x) / 2)
    return (sorted_input[middle - 1] + sorted_input[middle]) / 2


def median_hard(x, k):
    fence = x[0]
    side_a = []
    side_b = []
    on_fence = []

    for element in x:
        if element < fence:
            side_a.append(element)
        elif element > fence:
            side_b.append(element)
        else:
            on_fence.append(element)  # can do it without this

    if k <= len(side_a):
        return median_hard(side_a, k)
    elif k > len(side_a) + len(on_fence):
        return median_hard(side_b, k - (len(side_a) + len(on_fence)))
    else:
        return fence


print(median_supereasy(input_array))
print(median_easy(input_array))
print(median_hard(input_array, len(input_array) / 2))
