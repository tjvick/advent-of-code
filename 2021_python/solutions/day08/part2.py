from solutions import helpers

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

mappings = {
    0: 'ABCEFG',
    1: 'CF',
    2: 'ACDEG',
    3: 'ACDFG',
    4: 'BCDF',
    5: 'ABDFG',
    6: 'ABDEFG',
    7: 'ACF',
    8: 'ABCDEFG',
    9: 'ABCDFG'
}

uniques = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

count = 0
output_value_sum = 0
for string in strings:
    observed, output = string.split('|')
    observed_digits = observed.strip().split(' ')
    output_digits = output.strip().split(' ')
    all_digits = observed_digits + output_digits

    print(all_digits)
    ix_unique_digits = [ix for ix, digit in enumerate(all_digits) if len(digit) in uniques.keys()]
    print(ix_unique_digits)

    unique_digits_found = [all_digits[ix] for ix in ix_unique_digits]
    print(unique_digits_found)

    unique_digits = [uniques[len(all_digits[ix])] for ix in ix_unique_digits]
    print(unique_digits)

    one = set(unique_digits_found[unique_digits.index(1)])
    four = set(unique_digits_found[unique_digits.index(4)])
    seven = set(unique_digits_found[unique_digits.index(7)])
    eight = set(unique_digits_found[unique_digits.index(8)])

    print(one, four, seven, eight)
    alpha = eight - seven - four
    beta = one
    delta = seven - four
    gamma = four - one
    tau = eight - four

    print(alpha, beta, delta, gamma, tau)

    output_value_string = ''
    for output_digit in output_digits:
        print(output_digit)

        if len(output_digit) in uniques:
            number = uniques[len(output_digit)]
        elif len(output_digit) == 5:
            if set(output_digit).intersection(set().union(beta, delta)) == set().union(beta, delta):
                number = 3
            elif set(output_digit).intersection(set().union(delta, gamma)) == set().union(delta, gamma):
                number = 5
            else:
                number = 2
        elif len(output_digit) == 6:
            if set(output_digit).intersection(set().union(alpha, gamma)) == set().union(alpha, gamma):
                number = 6
            elif set(output_digit).intersection(set().union(tau, beta)) == set().union(tau, beta):
                number = 0
            else:
                number = 9

        output_value_string += str(number)

    output_value = int(output_value_string)
    print(output_value)

    output_value_sum += output_value

print(output_value_sum)



