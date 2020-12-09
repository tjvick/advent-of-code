import numpy as np

with open('input', 'r') as f:
    numbers = np.array([int(line.strip('\n')) for line in f])

target_sum = 177777905
# target = 127

done = False
for sum_size in range(2, len(numbers)):
    for ix in range(len(numbers) - sum_size):
        window = numbers[ix:ix+sum_size]
        window_sum = sum(window)
        if window_sum == target_sum:
            print(window)
            print(min(window) + max(window))
            done = True
            break

    if done:
        break

