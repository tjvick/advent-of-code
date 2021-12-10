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


def read_each_line_as_delimited_int_sequence(filepath, delimiter=None, dtype=int):
    integer_lists = []
    with open(filepath, 'r') as f:
        for line in f:
            integer_lists.append(np.array(line.strip('\n').split(delimiter), dtype=dtype))

    return integer_lists


def bit_sequence_to_int(bit_sequence):
    return int("".join(map(str, bit_sequence)), 2)


def find_local_minimum(f_x, x_0, x_min, x_max, step=1):
    x = x_0
    y_0 = f_x(x)
    y_1 = f_x(x + step)

    count = 0

    if y_1 < y_0:
        direction = 1
        bound = x_max
    elif y_1 > y_0:
        direction = -1
        bound = x_min
    else:
        print("No Variation at start!")
        return x_0, y_0, -1

    prev = y_0
    while direction*x < direction*bound:
        count += 1
        x += direction*step
        if f_x(x) > prev:
            return x-direction*step, prev, 0
        prev = f_x(x)

    print("Boundary reached: ", bound)
    return x_0, y_0, -1


def find_local_minimum_fast(f_x, x_0, x_min, x_max, step_sizes=(10, 1)):
    result = None
    for step_size in step_sizes:
        result = find_local_minimum(f_x, x_0, x_min, x_max, step=step_size)
        x_0 = result[0]

    return result
