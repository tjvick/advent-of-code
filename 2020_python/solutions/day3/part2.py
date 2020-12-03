with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

n_lines = len(file_contents)
line_width = len(file_contents[0])


def count_trees(right_step, down_step):
    n_trees = 0
    column_counter = 0
    row_counter = 0
    while row_counter < n_lines:
        char = file_contents[row_counter][column_counter]

        if char == '#':
            n_trees += 1

        row_counter += down_step
        column_counter = (column_counter + right_step) % line_width

    return n_trees


product = count_trees(1, 1)*count_trees(3, 1)*count_trees(5, 1)*count_trees(7, 1)*count_trees(1, 2)
print(product)

