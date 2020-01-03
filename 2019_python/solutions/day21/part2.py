import sys
sys.path.append('..')
from shared.intcode import IntCode


def render(x):
    try:
        print(''.join([chr(char_code) for char_code in x]))
    except ValueError:
        print(''.join([chr(char_code) for char_code in x[:-1]]))
        return x[-1]


def apply_rules(pattern):
    for ix in range(8):
        t, j = [False, False]
        a, b, c, d, e, f, g, h, i = [bool(x) for x in pattern[ix + 1:ix + 10]]
        t = not t
        t = a and t
        t = b and t
        t = c and t
        t = not t
        t = d and t
        j = e or j
        j = h or j
        j = t and j
        if j:
            return ix


def program_springbot(content):
    raw_program = list(map(lambda x: int(x), content.split(',')))

    p = IntCode(raw_program)
    p.run(True)

    instructions = [
        "NOT T T",
        "AND A T",
        "AND B T",
        "AND C T",
        "NOT T T",
        "AND D T",
        "OR E J",
        "OR H J",
        "AND T J",
        "RUN"
    ]

    instructions_encoded = []
    for instruction in instructions:
        instructions_encoded += [ord(c) for c in instruction+"\n"]

    p.inputs = instructions_encoded
    p.run(True)
    return render(p.outputs)


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return program_springbot(content)


if __name__ == "__main__":
    print(main())
