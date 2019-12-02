with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        program = list(map(lambda x: int(x), content.split(',')))

        program[1] = 12
        program[2] = 2
        read_pos = 0
        while read_pos >= 0:
            opcode = program[read_pos]
            if opcode != 99:
                value1 = program[program[read_pos+1]]
                value2 = program[program[read_pos+2]]
                if opcode == 1:
                    value3 = value1 + value2
                elif opcode == 2:
                    value3 = value1 * value2

                program[program[read_pos+3]] = value3
                read_pos += 4
            else:
                read_pos = -1

        print(program)

