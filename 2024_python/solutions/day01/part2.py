from collections import Counter

from solutions import helpers

filepath = 'input'

lists_as_2d_array = helpers.read_as_2d_array_of_delimited_values(filepath)

left_list = lists_as_2d_array[:,0]
right_list = lists_as_2d_array[:,1]

left_element_counter = Counter(left_list)
right_element_counter = Counter(right_list)

total_similarity = 0

list_intersection = set(left_list).intersection(set(right_list))
for element in list_intersection:
    left_count = left_element_counter[element]
    right_count = right_element_counter[element]

    similarity_increase = element * left_count * right_count

    total_similarity += similarity_increase

print(total_similarity)