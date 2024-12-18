from solutions import helpers

filepath = 'input'
# filepath = 'test1'

input_lines = helpers.read_each_line_as_string(filepath)

program = [int(_) for _ in input_lines[4].split(': ')[1].split(',')]

def run_program(a):
    register_a_value = a
    register_b_value = 0
    register_c_value = 0

    instruction_pointer = 0
    output_values = []

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

    while True:
        if instruction_pointer >= len(program):
            return output_values

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


current_a_guess = 0
for place in range(len(program)+1):
    for addon in range(64):
        result = run_program(current_a_guess + addon)
        # print(current_a_guess + addon, result, program[-place-1:])
        if result == program[-place-1:]:
            current_a_guess = current_a_guess + addon
            break

    if run_program(current_a_guess) == program:
        print("DONE!", current_a_guess)
    else:
        current_a_guess = current_a_guess * 8
        continue
