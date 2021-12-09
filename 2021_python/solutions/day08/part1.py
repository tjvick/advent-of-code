from solutions import helpers

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

unique_segment_counts = [2, 3, 4, 7]

n_easy_digits = 0
count_with_every_unique = 0
for string in strings:
    observed_digits, output_digits = (x.split() for x in string.split(' | '))
    n_easy_digits += sum(len(digit) in unique_segment_counts for digit in output_digits)

    digit_lengths = map(len, observed_digits)
    count_with_every_unique += set(unique_segment_counts).issubset(digit_lengths)


print('answer:', n_easy_digits)

print(count_with_every_unique == len(strings))
