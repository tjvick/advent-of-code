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

    instructions = [
        "NOT A T",
        "NOT B J",
        "OR T J",
        "NOT C T",
        "OR T J",
        "AND D J",
        "WALK"
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
