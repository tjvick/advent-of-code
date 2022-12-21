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
        try:
            matches_number = re.match(r'-?\d+', self.job)
            if matches_number:
                return int(self.job)

            matches_operation = re.match(r'(\w+) (.{1,2}) (\w+)', self.job)
            if matches_operation:
                id1, operation, id2 = matches_operation.groups()
                value1 = monkeys[id1].evaluate(monkeys)
                value2 = monkeys[id2].evaluate(monkeys)
                return eval(f'{value1} {operation} {value2}')
            else:
                print(self.id, self.job)
        except Exception as e:
            # print(self.job)
            raise e


monkeys: dict[str, Monkey] = {}

for string in strings:
    m = re.match(r'(\w+): (.+)', string)
    monkey_id, job = m.groups()

    if monkey_id == "root":
        job = re.sub(r'[+\-*/]', '-', job)

    monkey = Monkey(id=monkey_id, job=job)
    monkeys[monkey_id] = monkey


def compute_root_value(humn_value):
    monkeys['humn'].job = str(humn_value)
    return monkeys["root"].evaluate(monkeys)


def compute_val_and_slope(xa):
    xb = xa+1
    ya = compute_root_value(xa)
    yb = compute_root_value(xb)
    dy = yb - ya
    return ya, dy


def find_root():
    xa = 0
    while True:
        ya, dy = compute_val_and_slope(xa)
        print(ya, dy)
        if ya == 0:
            return xa
        else:
            xa = int(xa - ya / dy)


print('Answer', find_root())
