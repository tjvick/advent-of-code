from solutions import helpers

filename = 'input'

values = helpers.read_as_int_list(filename)

count = 0
for ix, value in enumerate(values[3:]):
    if value > values[ix]:
        count += 1

print(count)

