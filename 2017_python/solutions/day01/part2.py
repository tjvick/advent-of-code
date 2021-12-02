from solutions import helpers

filename = 'input'

[values] = helpers.read_as_digit_lists(filename)

half = int(len(values) / 2)
total = 0
for ix, value in enumerate(values):
    if value == values[(ix+half) % len(values)]:
        total += value

print(total)
