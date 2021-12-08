from solutions import helpers

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

mappings = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

uniques = mappings.keys()

count = 0
count_with_every_unique = 0
for string in strings:
    observed, output = string.split('|')
    output_digits = output.strip().split(' ')
    observed_digits = observed.strip().split(' ')
    count += sum(len(digit) in mappings for digit in output_digits)

    unique_lengths = set(len(digit) for digit in observed_digits)
    count_with_every_unique += all(x in unique_lengths for x in mappings.keys())

print('answer:', count)

print(count_with_every_unique == len(strings))





