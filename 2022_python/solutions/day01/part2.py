from solutions import helpers
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

all_calorie_totals = []
elf_calorie_total = 0
for s in strings:
    if s == '':
        all_calorie_totals.append(elf_calorie_total)
        elf_calorie_total = 0
    else:
        elf_calorie_total += int(s)

all_calorie_totals.append(elf_calorie_total)

top_totals = sorted(all_calorie_totals, reverse=True)[0:3]
print(sum(top_totals))
