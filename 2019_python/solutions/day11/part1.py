import sys
sys.path.append('..')
from shared.intcode import IntCode


def do_the_thing(content):
    raw_program = list(map(lambda x: int(x), content.split(',')))
    p = IntCode(raw_program)

    grid = dict()
    position = (0, 0)
    facing = 0
    visited = set()
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
            position = (position[0], position[1] - 1)
        elif facing == 1:
            position = (position[0] + 1, position[1])
        elif facing == 2:
            position = (position[0], position[1] + 1)
        elif facing == 3:
            position = (position[0] - 1, position[1])

        if done:
            print('done')

    return len(grid.keys())


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
