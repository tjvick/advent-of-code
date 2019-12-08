import numpy as np

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')

x = np.array(list(content))
a = x.reshape([100, 6, 25])

b = np.empty([6, 25], dtype=str)
for ir in range(6):
    for ic in range(25):
        stack = a[0:100, ir, ic]
        val = " "
        print(stack)
        for ix, el in enumerate(stack):
            if el == '2':
                val = val
            elif el == '0':
                val = " "
                break
            elif el == '1':
                val = "O"
                break
        print(val)
        b[ir, ic] = val

for row in b:
    print(''.join(row))


