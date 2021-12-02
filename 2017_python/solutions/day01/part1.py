from solutions import helpers

filename = 'input'

[values] = helpers.read_as_digit_lists(filename)

total = 0
for ix, value in enumerate(values):
    if value == values[(ix+1) % len(values)]:
        total += value

print(total)


