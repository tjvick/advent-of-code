import numpy as np

with open('input', 'r') as f:
    numbers = np.array([int(line.strip('\n')) for line in f])

window_size = 25

for ix, number in enumerate(numbers[window_size:]):
    window = numbers[ix:ix + window_size]
    diff = number - window
    pairs = np.setdiff1d(
        np.intersect1d(diff, window),
        [number]
    )
    if len(pairs) == 0:
        print(number)
