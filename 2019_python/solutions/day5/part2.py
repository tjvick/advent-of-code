import re

with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        program = list(map(lambda x: int(x), content.split(',')))

input = 5
read_pos = 0
while read_pos >= 0:
    opcode = program[read_pos]
    opcode_str = "{:05d}".format(opcode)
    instruction = int(opcode_str[3:5])
    mode_1 = int(opcode_str[2])
    mode_2 = int(opcode_str[1])
    mode_3 = int(opcode_str[0])

    if instruction == 99:
        read_pos = -1
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
        program[program[read_pos+1]] = input
        read_pos += 2
    elif instruction == 4:
        print("error:", program[program[read_pos+1]])
        read_pos += 2
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