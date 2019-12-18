import sys
import numpy as np
sys.path.append('..')
from shared.intcode import IntCode


def render_image(ascii_codes):
    image_chars = ""
    for code in ascii_codes:
        if code == 35:
            char = "#"
        elif code == 46:
            char = "."
        elif code == 10:
            char = "\n"

        image_chars += char

    print(image_chars)


def convert_image_to_pos_data(ascii_codes):
    image_data = dict()
    ir = 0
    ic = -1
    for code in ascii_codes:
        if code == 35:
            char = "#"
            ic += 1
        elif code == 46:
            char = "."
            ic += 1
        elif code == 10:
            char = "\n"
            ir += 1
            ic = -1

        image_data[(ir, ic)] = code

    print(image_data)
    return image_data


def get_char_code(positions, position, dr, dc):
    new_pos = (position[0]+dr, position[1]+dc)
    if new_pos in positions:
        return positions[new_pos]

    return -1


def do_the_thing(content):
    raw_program = list(map(lambda x: int(x), content.split(',')))
    p = IntCode(raw_program)
    p.run_out()

    render_image(p.outputs)
    positions = convert_image_to_pos_data(p.outputs)

    alignment_parameters = []
    for position, char in positions.items():
        top_char = get_char_code(positions, position, -1, 0)
        bottom_char = get_char_code(positions, position, 1, 0)
        left_char = get_char_code(positions, position, 0, -1)
        right_char = get_char_code(positions, position, 0, 1)
        if top_char == bottom_char == left_char == right_char == char == 35:
            print(position)
            alignment_parameter = position[0] * position[1]
            alignment_parameters.append(alignment_parameter)

    return sum(alignment_parameters)


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
