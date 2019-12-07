import sys
sys.path.append('..')
from shared.intcode import run_intcode

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        program = list(map(lambda x: int(x), content.split(',')))

output, _, _ = run_intcode(program, [5])
print(output)