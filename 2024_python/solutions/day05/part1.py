from collections import defaultdict
from functools import cmp_to_key

filepath = 'input'
# filepath = 'test'

required_prior_pages = defaultdict(list)
required_after_pages = defaultdict(list)
updates = []

with open(filepath, 'r') as f:
    for line in f:
        if '|' in line:
            a, b = line.strip('\n').split('|')
            required_prior_pages[b].append(a)
            required_after_pages[a].append(b)
        if ',' in line:
            update = line.strip('\n').split(',')
            updates.append(update)

def comparator(a, b):
    if a in required_prior_pages[b]:
        return -1
    if b in required_after_pages[a]:
        return 1
    return 0

valid_middle_page_sum = 0

for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(comparator))
    is_update_valid = update == sorted_update

    if is_update_valid:
        middle_index = int(len(update) / 2)
        valid_middle_page_sum += int(update[middle_index])

print(valid_middle_page_sum)