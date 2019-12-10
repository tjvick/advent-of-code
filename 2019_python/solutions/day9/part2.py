import sys
sys.path.append('..')
from shared.intcode import IntCode


def run_program(string_program, input):
    raw_program = list(map(lambda x: int(x), string_program.split(',')))
    p = IntCode(raw_program)
    return p.run_out(input)


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return run_program(content, 2)[0]


if __name__ == "__main__":
    print(main())
