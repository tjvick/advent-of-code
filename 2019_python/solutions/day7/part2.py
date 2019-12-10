import itertools
import sys
sys.path.append('..')
from shared.intcode import IntCode


def find_max_output(string_program):
    raw_program = list(map(lambda x: int(x), string_program.split(',')))

    max_output = 0
    perms = itertools.permutations(range(5, 10))
    for perm in perms:
        input = 0
        programs = []
        for ix, phase in enumerate(perm):
            p = IntCode(raw_program, [phase])
            input, _ = p.run_io(input)
            programs.append(p)

        done = False
        while not done:
            for ix, phase in enumerate(perm):
                input, done = programs[ix].run_io(input)

        round_output = input
        print(round_output)

        max_output = max(round_output, max_output)

    return max_output


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return find_max_output(content)


if __name__ == "__main__":
    print(main())