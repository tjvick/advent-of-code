import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)


def read_as_2d_array_of_delimited_values(filepath, delimiter=None, dtype=int):
    with open(filepath, 'r') as f:
        integer_lists = []
        for line in f:
            integer_lists.append(line.strip('\n').split(delimiter))

        return np.asarray(integer_lists, dtype=dtype)


def read_as_list_of_delimited_arrays(filepath, delimiter=None, dtype=int):
    integer_lists = []
    with open(filepath, 'r') as f:
        for line in f:
            integer_lists.append(np.array(line.strip('\n').split(delimiter), dtype=dtype))

    return integer_lists


def read_as_2d_array_of_characters(filepath, dtype=str):
    with open(filepath, 'r') as f:
        character_lists = [list(line.strip('\n')) for line in f]

    return np.asarray(character_lists, dtype=dtype)


def read_each_line_as_string(filepath):
    with open(filepath, 'r') as f:
        return [line.strip('\n') for line in f]