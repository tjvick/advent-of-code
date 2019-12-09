import itertools
import sys
sys.path.append('..')
from shared.intcode import run_intcode

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        raw_program = list(map(lambda x: int(x), content.split(',')))

dict_program = dict(x for x in enumerate(raw_program))
print(dict_program)
output, _, _ = run_intcode(dict_program, [2])

print(output)