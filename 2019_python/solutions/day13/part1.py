import sys
sys.path.append('..')
from shared.intcode import IntCode


def do_the_thing(content):
    raw_program = list(map(lambda x: int(x), content.split(',')))

    p = IntCode(raw_program)

    p.inputs = []
    done = p.run()
    instructions = p.outputs

    n_blocks = 0
    ix = 0
    while ix < len(instructions):
        instructions[ix]
        instructions[ix+1]
        tile_id = instructions[ix+2]
        if tile_id == 2:
            n_blocks += 1
        ix += 3

    print(n_blocks)


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
