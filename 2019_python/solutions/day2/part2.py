with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        for noun in range(0, 100):
            for verb in range(0, 100):
                program = list(map(lambda x: int(x), content.split(',')))
                program[1] = noun
                program[2] = verb

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

                if program[0] == 19690720:
                    print('HEY WE DID IT!: ', 100 * noun + verb)

