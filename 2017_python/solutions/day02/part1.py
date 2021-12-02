from solutions import helpers

filename = 'input'

integer_lists = helpers.read_as_delimited_integer_lists(filename)

print(integer_lists)

checksum = 0
for integer_list in integer_lists:
    checksum += max(integer_list) - min(integer_list)

print(checksum)


