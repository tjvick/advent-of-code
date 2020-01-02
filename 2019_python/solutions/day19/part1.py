import sys
sys.path.append('..')
from shared.intcode import IntCode


def do_the_thing(content):
    raw_program = list(map(lambda x: int(x), content.split(',')))

    total_affected = 0
    for y in range(50):
        for x in range(50):
            p = IntCode(raw_program)
            p.inputs = [x, y]
            out, done = p.run_io([x, y])
            total_affected += out

    return total_affected


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
