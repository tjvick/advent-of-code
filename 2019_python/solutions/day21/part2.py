import sys
sys.path.append('..')
from shared.intcode import IntCode


def render(x):
    try:
        print(''.join([chr(char_code) for char_code in x]))
    except ValueError:
        print(''.join([chr(char_code) for char_code in x[:-1]]))
        return x[-1]


def do_the_thing(content):
    raw_program = list(map(lambda x: int(x), content.split(',')))

    p = IntCode(raw_program)
    done = p.run(True)
    print('done?', done)
    render(p.outputs)

    instructions = [  # 00
        "NOT T T",  # 10
        "AND A T",  # 00
        "AND B T",  # 00
        "AND C T",  # 00
        "NOT T J",  # 01
        "AND D J",  # 01
        # second half
        "NOT J T",  # 11
        "NOT T T",  # 01
        "AND E T",  # 11
        "AND F T",  # 01
        "AND G T",  # 01
        "NOT T T",  # 11
        "AND H T",  # 01
        "OR T J",   # 01
        "AND D J",
        "RUN"
    ]
    instructions_encoded = []
    for instruction in instructions:
        instructions_encoded += [ord(c) for c in instruction+"\n"]

    p.inputs = instructions_encoded
    done = p.run(True)
    print('done?', done)
    return render(p.outputs)


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
