from solutions import helpers
import numpy as np

filename = 'input'

int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename, delimiter=",")

start = int_sequences[0]

n_days = 80
cycle = 7
fishes = start
for day in range(n_days):
    new_fishes = []
    for ix, fish in enumerate(fishes):
        if fishes[ix] == 0:
            new_fishes.append(8)
        fishes[ix] = (fishes[ix] - 1) % 7 if fishes[ix] < 0 else fishes[ix] - 1

    fishes = np.concatenate((fishes, new_fishes))

print(len(fishes))



