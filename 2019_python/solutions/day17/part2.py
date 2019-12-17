import sys
import numpy as np
sys.path.append('..')
from shared.intcode import IntCode


def render_image(ascii_codes):
    image_chars = ""
    for code in ascii_codes:
        char = chr(code)

        image_chars += char

    print(image_chars)


def get_char_code(positions, position, dr, dc):
    new_pos = (position[0]+dr, position[1]+dc)
    if new_pos in positions:
        return positions[new_pos]

    return -1


def do_the_thing(content):
    raw_program = list(map(lambda x: int(x), content.split(',')))
    raw_program[0] = 2
    p = IntCode(raw_program)
    main_program = "A,B,A,C,B,A,C,B,A,C\n"
    function_A = "L,6,L,4,R,12\n"
    function_B = "L,6,R,12,R,12,L,8\n"
    function_C = "L,6,L,10,L,10,L,6\n"
    print_output = "n\n"
    p.inputs += [ord(c) for c in list(main_program)]
    p.inputs += [ord(c) for c in list(function_A)]
    p.inputs += [ord(c) for c in list(function_B)]
    p.inputs += [ord(c) for c in list(function_C)]
    p.inputs += [ord(c) for c in list(print_output)]
    p.run_out()

    render_image(p.outputs)

    return p.outputs[-1]


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
