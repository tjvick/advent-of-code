import sys
sys.path.append('..')
from shared.intcode import run_intcode


def run_program(string_program, inputs):
    raw_program = list(map(lambda x: int(x), string_program.split(',')))
    dict_program = dict(x for x in enumerate(raw_program))
    output, _, _ = run_intcode(dict_program, inputs)
    return output


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return run_program(content, [2])


if __name__ == "__main__":
    print(main())
