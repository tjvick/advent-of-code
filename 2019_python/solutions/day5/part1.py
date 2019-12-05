import re

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        program = list(map(lambda x: int(x), content.split(',')))

print(program)

input = 1
read_pos = 0
while read_pos >= 0:
    opcode = program[read_pos]
    opcode_str = "{:05d}".format(opcode)
    instruction = int(opcode_str[3:5])

    if instruction == 99:
        read_pos = -1
    elif instruction == 3:
        program[program[read_pos+1]] = input
        read_pos += 2
    elif instruction == 4:
        print("error:", program[program[read_pos+1]])
        read_pos += 2
    else:
        mode_1 = int(opcode_str[2])
        mode_2 = int(opcode_str[1])
        mode_3 = int(opcode_str[0])

        value1 = program[program[read_pos+1]] if mode_1 == 0 else program[read_pos+1]
        value2 = program[program[read_pos+2]] if mode_2 == 0 else program[read_pos+2]
        if instruction == 1:
            value3 = value1 + value2
        elif instruction == 2:
            value3 = value1 * value2

        # assume position mode for the write
        # if mode_3 == 0:
        program[program[read_pos+3]] = value3
        # else:
        #     program[read_pos+3] = value3

        read_pos += 4