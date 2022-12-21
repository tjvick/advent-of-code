import dataclasses

from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)


@dataclasses.dataclass
class Monkey:
    id: str
    job: str

    def evaluate(self, monkeys):
        matches_number = re.match(r'\d+', self.job)
        if matches_number:
            return int(self.job)

        matches_operation = re.match(r'(\w+) (.) (\w+)', self.job)
        id1, operation, id2 = matches_operation.groups()
        value1 = monkeys[id1].evaluate(monkeys)
        value2 = monkeys[id2].evaluate(monkeys)
        return eval(f'{value1} {operation} {value2}')


monkeys: dict[str, Monkey] = {}

for string in strings:
    m = re.match(r'(\w+): (.+)', string)
    monkey_id, job = m.groups()
    monkey = Monkey(id=monkey_id, job=job)
    monkeys[monkey_id] = monkey

print(monkeys)
print(monkeys["root"].evaluate(monkeys))
