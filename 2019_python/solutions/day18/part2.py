
def do_the_thing(content):
    listified = list(map(lambda x: int(x), content.split(',')))
    return None


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
