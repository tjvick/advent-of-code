from solutions import helpers
import numpy as np

filepath = 'input'

lists_as_2d_array = helpers.read_as_2d_array_of_delimited_values(filepath)

left_list_sorted = np.sort(lists_as_2d_array[:,0])
right_list_sorted = np.sort(lists_as_2d_array[:,1])

difference = abs(left_list_sorted - right_list_sorted)

total_difference = sum(difference)
print(total_difference)