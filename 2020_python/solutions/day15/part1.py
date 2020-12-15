input = '0,12,6,13,20,1,17'
# input = '0,3,6'

starting_numbers = [int(x) for x in input.split(',')]

last_recorded = {}
for ix, number in enumerate(starting_numbers):
    last_recorded[number] = ix

print(last_recorded)

last_number = starting_numbers[-1]
first_occurrence = True
for ix in range(2020-len(starting_numbers)):
    c = ix+len(starting_numbers)
    if first_occurrence:
        spoken = 0
    else:
        # print(last_recorded)
        spoken = c - last_occurrence - 1

    if spoken not in last_recorded:
        first_occurrence = True
    else:
        first_occurrence = False
        last_occurrence = last_recorded[spoken]

    # print('spoken', spoken)
    last_recorded[spoken] = c
    last_number = spoken

# print(last_recorded)
print(last_number)
