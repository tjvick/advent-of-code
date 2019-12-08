import numpy as np

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')


def paint(stack):
    for el in stack:
        if el == '0':
            break
        elif el == '1':
            return "#"
    return " "


nr = 6
nc = 25
nl = int(len(content)/nr/nc)

a = np.array(list(content)).reshape([nl, nr, nc])

for ir in range(nr):
    painted_row = (paint(a[:, ir, ic]) for ic in range(nc))
    print(''.join(painted_row))
