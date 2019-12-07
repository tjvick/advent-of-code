TERMINATE = 99
INPUT = 3
OUTPUT = 4

value_write_cases = {
    1: lambda a, b: a + b,
    2: lambda a, b: a * b,
    7: lambda a, b: 1 if a < b else 0,
    8: lambda a, b: 1 if a == b else 0
}

jump_cases = {
    5: lambda a, b, ix: b if a != 0 else ix + 3,
    6: lambda a, b, ix: b if a == 0 else ix + 3
}


def run_intcode(program, inputs, init_pos=0):
    input_ix = 0
    read_pos = init_pos
    while read_pos >= 0:
        opcode = program[read_pos]
        opcode_str = "{:05d}".format(opcode)
        instruction = int(opcode_str[3:5])
        mode_1 = int(opcode_str[2])
        mode_2 = int(opcode_str[1])
        mode_3 = int(opcode_str[0])

        if instruction == TERMINATE:
            return "done", program, read_pos
        elif instruction == INPUT:
            program[program[read_pos + 1]] = inputs[input_ix]
            input_ix += 1
            read_pos += 2
        elif instruction == OUTPUT:
            output = program[program[read_pos + 1]]
            read_pos += 2
            return output, program, read_pos
        elif instruction in jump_cases.keys():
            (value1, value2) = values(program, read_pos, mode_1, mode_2)

            read_pos = jump_cases[instruction](value1, value2, read_pos)
        elif instruction in value_write_cases.keys():
            (value1, value2) = values(program, read_pos, mode_1, mode_2)
            position3 = position(program, mode_3, read_pos + 3)

            program[position3] = value_write_cases[instruction](value1, value2)
            read_pos += 4


def position(program, mode, ix):
    return program[ix] if mode == 0 else ix


def values(program, read_pos, *modes):
    return (program[position(program, mode, read_pos + ix + 1)] for ix, mode in enumerate(modes))

