import numpy as np

with open('input.txt', 'r') as f:
    instruction_text = [line.strip('\n') for line in f]


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
    op, arg = instruction.split(" ")
    return op, int(arg)


def run_program(instructions):
    execution_mask = np.zeros(len(instructions), dtype=bool)
    counter = 0
    accumulator = 0
    while True:
        execution_mask[counter] = True
        op, arg = instructions[counter]
        counter = change_counter[op](counter, arg)
        accumulator = change_accumulator[op](accumulator, arg)
        if counter >= len(execution_mask):
            print("YAY! ")
            print(accumulator)
            break
        if execution_mask[counter]:
            break



instructions = [parse_instruction(instruction) for instruction in instruction_text]

instruction_sets = []
for ix, (op, arg) in enumerate(instructions):
    if op == 'nop':
        new_instruction_set = instructions[:ix] + [('jmp', arg)] + instructions[ix+1:]
        instruction_sets.append(new_instruction_set)

    if op == 'jmp':
        new_instruction_set = instructions[:ix] + [('nop', arg)] + instructions[ix+1:]
        instruction_sets.append(new_instruction_set)

for instruction_set in instruction_sets:
    run_program(instruction_set)