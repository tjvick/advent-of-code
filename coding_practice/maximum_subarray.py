a = [-2, -3, 4, -1, -2, 1, 5, -3]

max_subarray_sum = a[0]
sum_ending_here = 0

for element in a:
    sum_ending_here += element
    if max_subarray_sum < sum_ending_here:
        max_subarray_sum = sum_ending_here

    if sum_ending_here < 0:
        sum_ending_here = 0

print(max_subarray_sum)