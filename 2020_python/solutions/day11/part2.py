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


def nearest_seats(ir, ic, bgrid):
    directions = [
        [-1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1],
        [-1, -1]
    ]

    seats = -1 * np.ones(8)
    for n_steps in range(1, max(bgrid.shape - np.array([ir, ic]))):
        # print("n_steps", n_steps)
        visible_area = [np.array([ir, ic]) + n_steps * np.array(step) for step in directions]
        for ix, index in enumerate(visible_area):
            # print('index', index)
            if seats[ix] >= 0:
                continue

            if index[0] < 0 or index[0] >= bgrid.shape[0]:
                seats[ix] = 0
                continue

            if index[1] < 0 or index[1] >= bgrid.shape[1]:
                seats[ix] = 0
                continue

            spot = bgrid[index[0], index[1]]
            if spot == 1:
                seats[ix] = 1
            elif spot == 2:
                seats[ix] = 2

        # print(seats)
        if not np.any(seats == -1):
            break

    return seats


def change(ir, ic, bgrid):
    new_val = bgrid[ir, ic]
    if bgrid[ir, ic] == 1:
        # no visible occupied seats
        seats = nearest_seats(ir, ic, bgrid)
        if sum(seats == 2) == 0:
            new_val = 2
    elif bgrid[ir, ic] == 2:
        # 5 other visibly occupied seats
        seats = nearest_seats(ir, ic, bgrid)
        if sum(seats == 2) >= 5:
            new_val = 1

    return new_val


def buffer(grid):
    buffgrid = np.zeros((grid.shape[0]+2, grid.shape[1]+2))
    buffgrid[1:grid.shape[0]+1, 1:grid.shape[1]+1] = grid
    return buffgrid


bgrid = buffer(grid)
print(bgrid.shape)

for ix in range(1000):
    print(ix)
    new_bgrid = bgrid.copy()
    for ir in range(grid.shape[0]):
        for ic in range(grid.shape[1]):
            new_val = change(ir+1, ic+1, bgrid)
            new_bgrid[ir+1, ic+1] = new_val

    if np.array_equal(new_bgrid, bgrid):
        print("done")
        print(sum(sum(bgrid == 2)))
        break

    # print(new_bgrid)
    bgrid = new_bgrid


# print("test")
test_seats = nearest_seats(2, 2, np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 0],
    [0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0],
    [0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0],
    [0, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 0],
    [0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0],
    [0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
    [0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 0],
    [0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
# print(test_seats)
