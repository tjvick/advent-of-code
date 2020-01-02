import sys
import math
sys.path.append('..')
from shared.intcode import IntCode


def find_change_along_x(program, x_lb, x_ub, y):
    p = IntCode(program)
    lb_value, _ = p.run_io([x_lb, y])

    while x_ub - x_lb > 1:
        x_search = math.floor((x_ub + x_lb) / 2)
        p = IntCode(program)
        out, _ = p.run_io([x_search, y])
        # print('x_search', x_search, out)
        if out == lb_value:
            x_lb = x_search
        else:
            x_ub = x_search

    return x_lb, x_ub


def find_change_along_y(program, x, y_lb, y_ub):
    p = IntCode(program)
    lb_value, _ = p.run_io([x, y_lb])

    while y_ub - y_lb > 1:
        y_search = math.floor((y_ub + y_lb) / 2)
        p = IntCode(program)
        out, _ = p.run_io([x, y_search])
        # print('y_search', y_search, out)
        if out == lb_value:
            y_lb = y_search
        else:
            y_ub = y_search

    return y_lb, y_ub


def find_beam_boundary(program, y):
    x_max = 10000
    x_lb = 0
    x_ub = x_max
    x_search_step = math.floor(y / 20)
    x_search = 0
    while True:
        # print('x_search', x_search)
        if x_search > x_max:
            break
        p = IntCode(program)
        out, _ = p.run_io([x_search, y])
        if out:
            x_lb = x_search
        if x_lb and not out:
            x_ub = x_search
            break
        x_search += x_search_step

    return x_lb, x_ub


def find_max_box_width(program, y):
    # find bounds of beam end in row
    x_lb, x_ub = find_beam_boundary(program, y)

    # find end of beam in row
    x_end, _ = find_change_along_x(program, x_lb, x_ub, y)
    # print('x_end', (y, x_end))

    # find end of beam in column
    y_end, _ = find_change_along_y(program, x_end, y, y*2)

    y_end = y + min(y_end-y, 99)
    # print('y_end', y_end)

    # find start of beam in row
    _, x_start = find_change_along_x(program, 0, x_end, y_end)
    # print('x_start', (y_end, x_start))

    height = y_end - y + 1
    width = x_end - x_start + 1
    print('box size at', y, ':', width, 'by', height)
    return width, x_start


def try_harder(content):
    program = list(map(lambda x: int(x), content.split(',')))

    lb = 0
    ub = 3000
    while ub - lb > 1:
        y = math.floor((lb + ub)/2)
        min_box_size, x_start = find_max_box_width(program, y)
        if min_box_size < 100:
            lb = y
        else:
            ub = y
            answer = x_start*10000 + y

    return answer


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return try_harder(content)


if __name__ == "__main__":
    print(main())
