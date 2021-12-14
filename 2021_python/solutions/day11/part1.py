from solutions import helpers
import numpy as np

filename = 'input'

digit_sequences = helpers.read_each_line_as_digit_sequence(filename)

octopuses = np.array(digit_sequences)

octopuses = np.concatenate((np.zeros((10, 1)), octopuses, np.zeros((10, 1))), axis=1)
octopuses = np.concatenate((np.zeros((1, 12)), octopuses, np.zeros((1, 12))), axis=0)

window = np.array([
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
])

total_flashes = 0
for n_steps in range(100):
    prev = np.zeros_like(octopuses)
    deltas = np.zeros_like(octopuses)

    deltas[1:11, 1:11] = 1
    diff = deltas - prev

    while np.sum(diff) > 0:
        prev = deltas.copy()
        for ir in range(1, 11):
            for ic in range(1, 11):
                # print(ir, ic)
                ix_neighbors = window + [ir, ic]
                n_over_limit = 0
                for ix_neighbor in ix_neighbors:
                    x, y = ix_neighbor[0], ix_neighbor[1]
                    if octopuses[x, y] + deltas[x, y] > 9:
                        n_over_limit += 1

                deltas[ir, ic] = 1 + n_over_limit

        diff = deltas - prev

    octopuses = octopuses + deltas
    total_flashes += np.sum(octopuses > 9)
    octopuses[octopuses > 9] = 0

    # print(octopuses[1:11, 1:11])
print(total_flashes)
