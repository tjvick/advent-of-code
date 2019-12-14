import sys
import numpy as np
sys.path.append('..')
from shared.intcode import IntCode


def do_the_thing(content):
    raw_program = list(map(lambda x: int(x), content.split(',')))
    raw_program[0] = 2

    p = IntCode(raw_program)
    p.inputs = []

    done = False
    while not done:
        done = p.run(True)
        # if not done:
        #     print('Still Playing...')
        instructions = p.outputs

        n_blocks = 0
        # screen = np.full([20, 50], ' ', dtype=object)

        current_score = 0
        ball_pos = 0
        paddle_pos = 0
        ix = 0
        while ix < len(instructions):
            ic = instructions[ix]
            ir = instructions[ix+1]
            tile_id = instructions[ix+2]
            if tile_id == 2:
                n_blocks += 1
            ix += 3
            if tile_id == 4:
                ball_pos = ic
            if tile_id == 3:
                paddle_pos = ic

            if ic == -1 and ir == 0:
                current_score = tile_id
            # else:
                # screen[ir, ic] = paint(tile_id)

        # draw(screen)
        # print(current_score)

        if not done:
            joystick_command = 0
            if ball_pos > paddle_pos:
                joystick_command = 1
            elif ball_pos < paddle_pos:
                joystick_command = -1
            p.inputs.append(joystick_command)

    return current_score


# def paint(tile_id):
#     if tile_id == 0:
#         return " "
#     elif tile_id == 1:
#         return "|"
#     elif tile_id == 2:
#         return "#"
#     elif tile_id == 3:
#         return '-'
#     elif tile_id == 4:
#         return "o"


# def draw(screen):
#     for ir in range(screen.shape[0]):
#         print(''.join(screen[ir]))


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
