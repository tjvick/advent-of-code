TERMINATE = 99
INPUT = 3
OUTPUT = 4
ADJUST_RELATIVE = 9

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
    relative_base = 0
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
            write_position = position(program, mode_1, read_pos+1, relative_base)
            program[write_position] = inputs[input_ix]
            input_ix += 1
            read_pos += 2
        elif instruction == OUTPUT:
            output = read(program, position(program, mode_1, read_pos + 1, relative_base))
            read_pos += 2
            print('output', output)
            return output, program, read_pos
        elif instruction == ADJUST_RELATIVE:
            relative_base += program[position(program, mode_1, read_pos + 1, relative_base)]
            read_pos += 2
        elif instruction in jump_cases.keys():
            (value1, value2) = values(program, read_pos, relative_base, mode_1, mode_2)

            read_pos = jump_cases[instruction](value1, value2, read_pos)
        elif instruction in value_write_cases.keys():
            (value1, value2) = values(program, read_pos, relative_base, mode_1, mode_2)
            position3 = position(program, mode_3, read_pos + 3, relative_base)
            program[position3] = value_write_cases[instruction](value1, value2)
            read_pos += 4


def position(program, mode, ix, relative_base):
    if mode == 0:  # position
        return program[ix]
    elif mode == 2:  # relative
        return program[ix]+relative_base
    else:  # immediate
        return ix


def values(program, read_pos, relative_base, *modes):
    return (read(program, position(program, mode, read_pos + ix + 1, relative_base)) for ix, mode in enumerate(modes))


def read(program, index):
    return program[index] if index in program else 0
