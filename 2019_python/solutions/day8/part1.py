from collections import Counter
import numpy as np

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')

x = np.array(list(content))
a = x.reshape([100, 6, 25])

max_zeros = 10000000
for il in range(100):
    count = 0
    b = (a[il][:][:]).flatten()
    c = Counter(b)
    print(len(b))
    n_zeros = c["0"]
    if n_zeros < max_zeros:
        max_zeros = n_zeros
        answer = c["1"]*c["2"]



