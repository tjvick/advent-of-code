import numpy as np

with open('input.txt', 'r') as f:
    instructions = [line.strip('\n') for line in f]


change_counter = {
    'nop': lambda counter, arg: counter + 1,
    'acc': lambda counter, arg: counter + 1,
    'jmp': lambda counter, arg: counter + arg
}

change_accumulator = {
    'nop': lambda acc, arg: acc,
    'acc': lambda acc, arg: acc + arg,
    'jmp': lambda acc, arg: acc
}


def parse_instruction(instruction):
    [op, arg] = instruction.split(" ")
    return (op, int(arg))

execution_mask = np.zeros(len(instructions), dtype=bool)


counter = 0
accumulator = 0
while True:
    execution_mask[counter] = True
    op, arg = parse_instruction(instructions[counter])
    counter = change_counter[op](counter, arg)
    accumulator = change_accumulator[op](accumulator, arg)
    if execution_mask[counter]:
        print(accumulator)
        break

