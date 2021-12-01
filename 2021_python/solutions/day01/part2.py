from solutions import helpers

filename = 'input'

values = helpers.read_as_numpy_array(filename)

print(sum(values[3:] - values[:-3] > 0))

