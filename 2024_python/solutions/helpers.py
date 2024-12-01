import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)


def read_as_2d_array_of_delimited_values(filepath, delimiter=None, dtype=int):
    with open(filepath, 'r') as f:
        integer_lists = []
        for line in f:
            integer_lists.append(line.strip('\n').split(delimiter))

        return np.asarray(integer_lists, dtype=dtype)