from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

input_lines = helpers.read_each_line_as_string(filepath)

register_a_value = int(input_lines[0].split(': ')[1])
register_b_value = int(input_lines[1].split(': ')[1])
register_c_value = int(input_lines[2].split(': ')[1])

program = [int(_) for _ in input_lines[4].split(': ')[1].split(',')]

instruction_pointer = 0

def combo(op):
    if op < 4:
        return op
    if op == 4:
        return register_a_value
    if op == 5:
        return register_b_value
    if op == 6:
        return register_c_value
    if op == 7:
        print("BROKEN! INVALID COMBO OPERAND")
    return

def dv(operand):
    numerator = register_a_value
    denominator = 2 ** combo(operand)
    result_of_division = numerator // denominator
    return result_of_division

def bxl(operand):
    return register_b_value ^ operand

def bst(operand):
    return combo(operand) % 8

def jnz(operand, pointer):
    if register_a_value == 0:
        return pointer + 2
    else:
        return operand

def bxc():
    return register_b_value ^ register_c_value

def out(operand):
    return combo(operand) % 8

output_values = []

while True:
    if instruction_pointer >= len(program):
        print("HALT, I AM REPTAR!")
        break

    current_opcode = program[instruction_pointer]
    current_operand = program[instruction_pointer+1]

    if current_opcode == 0:
        register_a_value = dv(current_operand)
        instruction_pointer += 2
    if current_opcode == 1:
        register_b_value = bxl(current_operand)
        instruction_pointer += 2
    if current_opcode == 2:
        register_b_value = bst(current_operand)
        instruction_pointer += 2
    if current_opcode == 3:
        instruction_pointer = jnz(current_operand, instruction_pointer)
    if current_opcode == 4:
        register_b_value = bxc()
        instruction_pointer += 2
    if current_opcode == 5:
        output_values.append(out(current_operand))
        instruction_pointer += 2
    if current_opcode == 6:
        register_b_value = dv(current_operand)
        instruction_pointer += 2
    if current_opcode == 7:
        register_c_value = dv(current_operand)
        instruction_pointer += 2


print(output_values)
print(','.join(str(_) for _ in output_values))




