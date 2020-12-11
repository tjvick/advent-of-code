import numpy as np

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

t = str.maketrans('L.', '10')

grid = []
for row in file_contents:
    grid.append([int(c) for c in row.translate(t)])

grid = np.array(grid)

# 0 - floor
# 1 - empty seat
# 2 - occupied seat
print(grid)


def change(ir, ic, bgrid):
    new_val = bgrid[ir, ic]
    if bgrid[ir, ic] == 1:
        if sum(sum(bgrid[ir-1:ir+2, ic-1:ic+2] == 2)) == 0:
            new_val = 2
    elif bgrid[ir, ic] == 2:
        if sum(sum(bgrid[ir-1:ir+2, ic-1:ic+2] == 2)) >= 5:
            new_val = 1

    return new_val



def buffer(grid):
    buffgrid = np.zeros((grid.shape[0]+2, grid.shape[1]+2))
    buffgrid[1:grid.shape[0]+1, 1:grid.shape[1]+1] = grid
    return buffgrid


bgrid = buffer(grid)

for ix in range(100000000):
    new_bgrid = bgrid.copy()
    for ir in range(grid.shape[0]):
        for ic in range(grid.shape[1]):
            new_val = change(ir+1, ic+1, bgrid)
            new_bgrid[ir+1, ic+1] = new_val

    if np.array_equal(new_bgrid, bgrid):
        print("done")
        print(ix)
        print(sum(sum(bgrid == 2)))
        break

    bgrid = new_bgrid

