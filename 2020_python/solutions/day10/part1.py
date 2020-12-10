import numpy as np
import collections

with open('input', 'r') as f:
    joltages = [int(line.strip('\n')) for line in f]


sorted_joltages = sorted(joltages)

print(sorted_joltages)

device_joltage = max(joltages) + 3
sorted_joltages.append(device_joltage)
sorted_joltages.insert(0, 0)

diffs = np.array(sorted_joltages[1:]) - np.array(sorted_joltages[:-1])

d = dict(collections.Counter(diffs))
print(d[1] * d[3])
