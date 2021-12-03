import numpy as np


def read_each_line_as_int(filepath):
    values = []
    with open(filepath, 'r') as f:
        for line in f:
            values.append(int(line.strip('\n')))

    return np.array(values)


def read_each_line_as_float(filepath):
    values = []
    with open(filepath, 'r') as f:
        for line in f:
            values.append(float(line.strip('\n')))

    return np.array(values)


def read_each_line_as_string(filepath):
    contents = []
    with open(filepath, 'r') as f:
        for line in f:
            contents.append(line.strip('\n'))

    return contents


def read_each_line_as_char_sequence(filepath):
    character_lists = []
    with open(filepath, 'r') as f:
        for line in f:
            character_lists.append(list(line.strip('\n')))

    return character_lists


def read_each_line_as_digit_sequence(filepath):
    digit_lists = []
    with open(filepath, 'r') as f:
        for line in f:
            digit_lists.append(np.array(list(line.strip('\n')), dtype=int))

    return digit_lists


def read_each_line_as_delimited_int_sequence(filepath, delimiter=None):
    integer_lists = []
    with open(filepath, 'r') as f:
        for line in f:
            integer_lists.append(np.array(line.strip('\n').split(delimiter), dtype=int))

    return integer_lists


def bit_sequence_to_int(bit_sequence):
    return int("".join(map(str, bit_sequence)), 2)