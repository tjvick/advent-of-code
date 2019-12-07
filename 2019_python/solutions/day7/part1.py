import itertools
import sys
sys.path.append('..')
from shared.intcode import run_intcode

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        raw_program = list(map(lambda x: int(x), content.split(',')))

max_output = 0
perms = itertools.permutations(range(5))
for perm in perms:
    output = 0
    for phase in perm:
        inputs = [phase, output]
        output, _, _ = run_intcode(raw_program, inputs)

    max_output = max(output, max_output)

print(max_output)