from solutions import helpers
filename = 'input'

values = helpers.read_each_line_as_float(filename)

print(sum(values[1:] - values[:-1] > 0))
