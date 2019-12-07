import itertools

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        raw_program = list(map(lambda x: int(x), content.split(',')))


def run_program(program, init_pos, inputs):
    input_ix = 0
    read_pos = init_pos
    while read_pos >= 0:
        opcode = program[read_pos]
        opcode_str = "{:05d}".format(opcode)
        instruction = int(opcode_str[3:5])
        mode_1 = int(opcode_str[2])
        mode_2 = int(opcode_str[1])
        mode_3 = int(opcode_str[0])

        if instruction == 99:
            return "done", program, read_pos
        elif instruction == 1:
            value1 = program[program[read_pos + 1]] if mode_1 == 0 else program[read_pos + 1]
            value2 = program[program[read_pos + 2]] if mode_2 == 0 else program[read_pos + 2]
            value3 = program[read_pos + 3] if mode_3 == 0 else read_pos + 3

            program[value3] = value1 + value2
            read_pos += 4
        elif instruction == 2:
            value1 = program[program[read_pos + 1]] if mode_1 == 0 else program[read_pos + 1]
            value2 = program[program[read_pos + 2]] if mode_2 == 0 else program[read_pos + 2]
            value3 = program[read_pos + 3] if mode_3 == 0 else read_pos + 3

            program[value3] = value1 * value2
            read_pos += 4
        elif instruction == 3:
            # print(read_pos)
            program[program[read_pos+1]] = inputs[input_ix]
            input_ix += 1
            read_pos += 2
        elif instruction == 4:
            output = program[program[read_pos+1]]
            # print("output:", output)
            read_pos += 2
            return output, program, read_pos
        elif instruction == 5:
            value1 = program[program[read_pos + 1]] if mode_1 == 0 else program[read_pos + 1]
            value2 = program[program[read_pos + 2]] if mode_2 == 0 else program[read_pos + 2]

            read_pos = value2 if value1 != 0 else read_pos+3
        elif instruction == 6:
            value1 = program[program[read_pos + 1]] if mode_1 == 0 else program[read_pos + 1]
            value2 = program[program[read_pos + 2]] if mode_2 == 0 else program[read_pos + 2]

            read_pos = value2 if value1 == 0 else read_pos+3
        elif instruction == 7:
            value1 = program[program[read_pos + 1]] if mode_1 == 0 else program[read_pos + 1]
            value2 = program[program[read_pos + 2]] if mode_2 == 0 else program[read_pos + 2]
            value3 = program[read_pos + 3] if mode_3 == 0 else read_pos + 3

            program[value3] = 1 if value1 < value2 else 0
            read_pos += 4
        elif instruction == 8:
            value1 = program[program[read_pos + 1]] if mode_1 == 0 else program[read_pos + 1]
            value2 = program[program[read_pos + 2]] if mode_2 == 0 else program[read_pos + 2]
            value3 = program[read_pos + 3] if mode_3 == 0 else read_pos + 3

            program[value3] = 1 if value1 == value2 else 0
            read_pos += 4


max_output = 0
perms = itertools.permutations(range(5, 10))
for perm in perms:
    print(perm)
    output = 0
    halted = False
    programs = []
    read_poss = []
    for phase in perm:
        output, program_ix, read_pos_ix = run_program(raw_program, 0, [phase, output])
        programs.append(program_ix.copy())
        read_poss.append(read_pos_ix)

    count = 0
    while not halted:
        count += 1
        for ix, phase in enumerate(perm):
            x, program_ix, read_pos_ix = run_program(programs[ix], read_poss[ix], [output])
            print(count, ix, x, program_ix)
            programs[ix] = program_ix.copy()
            read_poss[ix] = read_pos_ix
            if x == "done":
                halted = True
                round_output = output
                print(round_output)
                break
            output = x

    print(round_output)
    max_output = max(round_output, max_output)

print(max_output)