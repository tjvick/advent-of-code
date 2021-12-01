from solutions import helpers

filename = 'input'

values = helpers.read_as_int_list(filename)
print(values)

count = 0
prev_value = 100000000
for value in values:
    if value > prev_value:
        count += 1
    prev_value = value

print(count)

