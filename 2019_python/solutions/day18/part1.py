

def do_the_thing(content):
    return 8


def main(filename):
    with open(filename, 'r') as f:
        lines = [line.strip('\n') for line in f]

    return do_the_thing(lines)


if __name__ == "__main__":
    print(main('./input.txt'))
