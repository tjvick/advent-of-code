import itertools
import sys
sys.path.append('..')
from shared.intcode import run_intcode


def find_max_output(string_program):
    raw_program = list(map(lambda x: int(x), string_program.split(',')))
    dict_program = dict(x for x in enumerate(raw_program))

    max_output = 0
    perms = itertools.permutations(range(5))
    for perm in perms:
        output = 0
        for phase in perm:
            output, _, _ = run_intcode(dict_program, [phase, output])

        max_output = max(output, max_output)

    return max_output


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return find_max_output(content)


if __name__ == "__main__":
    print(main())
