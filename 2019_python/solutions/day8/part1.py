from collections import Counter
import numpy as np
from functools import reduce

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')

a = np.array(list(content)).reshape([100, 6, 25])


def reduce_fn(acc, layer):
    c = Counter(layer.flatten())
    if c['0'] < acc[0]:
        return c['0'], c['1']*c['2']
    return acc


result = reduce(reduce_fn, (layer for layer in a), (np.inf, 0))

print(result[1])


