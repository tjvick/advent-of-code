column = 0
n_trees = 0
with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        print(content[column])
        if content[column] == '#':
            n_trees += 1

        column = (column + 3) % len(content)

