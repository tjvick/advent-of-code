import sys
sys.path.append('..')
from shared.intcode import IntCode

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        program = list(map(lambda x: int(x), content.split(',')))
        dict_program = dict(x for x in enumerate(program))

p = IntCode(program)
output, _ = p.run_io(5)
print(output)