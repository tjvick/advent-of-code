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

screen = np.zeros((6, 40), dtype=str)

crt_position = 0
row = 0
for string in strings:
    # print(screen)
    # print(len(X_history))
    # print(string)
    if 'addx' in string:
        [_, addx_val] = string.split()
        if abs(X - crt_position) <= 1:
            screen[row, crt_position] = "#"
        else:
            screen[row, crt_position] = " "

        X_history.append(X)
        crt_position = (crt_position + 1) % 40
        if crt_position == 0:
            row += 1

        if abs(X - crt_position) <= 1:
            screen[row, crt_position] = "#"
        else:
            screen[row, crt_position] = " "
        X += int(addx_val)
        X_history.append(X)
        crt_position = (crt_position + 1) % 40
        if crt_position == 0:
            row += 1
    else:
        if abs(X - crt_position) <= 1:
            screen[row, crt_position] = "#"
        else:
            screen[row, crt_position] = " "
        X_history.append(X)
        crt_position = (crt_position + 1) % 40
        if crt_position == 0:
            row += 1


print(screen)
for row in screen:
    print(''.join(row))

