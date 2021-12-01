from solutions import helpers
filename = 'input'

values = helpers.read_as_numpy_array(filename)

print(sum(values[1:] - values[:-1] > 0))


