from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)


X = 1
X_history = [X]
cycle = 0
for string in strings:
    print(len(X_history))
    print(string)
    if 'addx' in string:
        [_, addx_val] = string.split()
        X_history.append(X)
        X += int(addx_val)
        X_history.append(X)
    else:
        X_history.append(X)

print(X_history)

total = 0
for ix in [20, 60, 100, 140, 180, 220]:
    print(ix, X_history[ix-1])
    total += X_history[ix-1] * ix

print(total)

