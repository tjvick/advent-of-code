from solutions import helpers

filename = 'input'

values = helpers.read_each_line_as_float(filename)

print(sum(values[3:] - values[:-3] > 0))
