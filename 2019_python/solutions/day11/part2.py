import sys
import numpy as np
sys.path.append('..')
from shared.intcode import IntCode


def do_the_thing(content):
    raw_program = list(map(lambda x: int(x), content.split(',')))
    p = IntCode(raw_program)

    grid = dict()
    position = (0, 0)
    grid[position] = 1
    facing = 0
    done = False
    while not done:
        see = grid[position] if position in grid else 0

        p.inputs = [see]
        done = p.run(True)

        color = p.outputs.pop(0)
        turn_direction = p.outputs.pop(0)

        # Paint
        grid[position] = color

        # Turn
        turn = -1 if turn_direction == 0 else 1
        facing = (facing + turn) % 4

        # Move
        if facing == 0:
            position = (position[0], position[1]-1)
        elif facing == 1:
            position = (position[0]+1, position[1])
        elif facing == 2:
            position = (position[0], position[1]+1)
        elif facing == 3:
            position = (position[0]-1, position[1])

        if done:
            print('done')

    paint(grid)


def paint(grid):
    print_grid = np.full([6, 43], '  ', dtype=object)

    for key, value in grid.items():
        print_grid[key[1], key[0]] = '  ' if value == 0 else 'TV'

    for row in print_grid:
        print(''.join(row))


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
