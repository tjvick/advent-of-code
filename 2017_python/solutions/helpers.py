import numpy as np


def read_as_int_list(filepath):
    values = []
    with open(filepath, 'r') as f:
        for line in f:
            values.append(int(line.strip('\n')))

    return values


def read_as_numpy_array(filepath):
    values = []
    with open(filepath, 'r') as f:
        for line in f:
            values.append(float(line.strip('\n')))

    return np.array(values)


def read_as_string_list(filepath):
    contents = []
    with open(filepath, 'r') as f:
        for line in f:
            contents.append(line.strip('\n'))

    return contents


def read_as_char_lists(filepath):
    character_lists = []
    with open(filepath, 'r') as f:
        for line in f:
            character_lists.append(list(line.strip('\n')))

    return character_lists


def read_as_digit_lists(filepath):
    digit_lists = []
    with open(filepath, 'r') as f:
        for line in f:
            digit_lists.append(np.array(list(line.strip('\n')), dtype=int))

    return digit_lists


def read_as_delimited_integer_lists(filepath, delimiter=None):
    integer_lists = []
    with open(filepath, 'r') as f:
        for line in f:
            integer_lists.append(np.array(line.strip('\n').split(delimiter), dtype=int))

    return integer_lists
