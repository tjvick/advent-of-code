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


def read_as_charset_list(filepath):
    character_sets = []
    with open(filepath, 'r') as f:
        for line in f:
            character_sets.append(list(line.strip('\n')))

    return character_sets


def read_as_digit_list(filepath):
    digit_sets = []
    with open(filepath, 'r') as f:
        for line in f:
            digit_sets.append(np.array(list(line.strip('\n')), dtype=int))

    return digit_sets