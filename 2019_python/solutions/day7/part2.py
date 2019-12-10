import itertools
import sys
sys.path.append('..')
from shared.intcode import run_intcode


def find_max_output(string_program):
    raw_program = list(map(lambda x: int(x), string_program.split(',')))
    dict_program = dict(x for x in enumerate(raw_program))

    max_output = 0
    perms = itertools.permutations(range(5, 10))
    for perm in perms:
        print(perm)
        input = 0
        programs = []
        read_poss = []
        for ix, phase in enumerate(perm):
            input, program_ix, read_pos_ix = run_intcode(dict_program, [phase, input])
            programs.append(program_ix.copy())
            read_poss.append(read_pos_ix)

        halted = False
        while not halted:
            for ix, phase in enumerate(perm):
                output, programs[ix], read_poss[ix] = run_intcode(programs[ix], [input], read_poss[ix])
                if output == "done":
                    halted = True
                    round_output = input
                    print(round_output)
                    break
                input = output

        max_output = max(round_output, max_output)

    return max_output


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return find_max_output(content)


if __name__ == "__main__":
    print(main())