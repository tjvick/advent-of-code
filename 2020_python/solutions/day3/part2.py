def do_it(row_step, col_step):
    row = 0
    column = 0
    n_trees = 0
    counter = 0

    with open('input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')
            if counter != row:
                counter += 1
                continue

            if content[column] == '#':
                n_trees += 1

            row = (row + row_step)
            column = (column + col_step) % len(content)
            counter += 1

    return n_trees

print(do_it(1, 1))
print(do_it(1, 3))
print(do_it(1, 5))
print(do_it(1, 7))
print(do_it(2, 1))
print(do_it(1, 1)*do_it(1, 3)*do_it(1, 5)*do_it(1, 7)*do_it(2, 1))

