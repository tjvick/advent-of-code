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


class IntCode:
    def __init__(self, program, inputs=[]):
        self.program = dict(x for x in enumerate(program))
        self.inputs = inputs
        self.outputs = []
        self.read_pos = 0
        self.relative_base = 0

    def run_io(self, x):
        x = x if type(x) == 'list' else [x]
        self.inputs = self.inputs + x
        done = self.run(True)
        return self.outputs.pop(0), done

    def run_out(self, x=None):
        if x is not None:
            self.inputs = self.inputs + (x if type(x) == 'list' else [x])
        self.run()
        return self.outputs

    def run(self, wait_for_inputs=False):
        while self.read_pos >= 0:
            opcode = self.program[self.read_pos]
            opcode_str = "{:05d}".format(opcode)
            instruction = int(opcode_str[3:5])
            mode_1 = int(opcode_str[2])
            mode_2 = int(opcode_str[1])
            mode_3 = int(opcode_str[0])

            if instruction == TERMINATE:
                return True
            elif instruction == INPUT:
                if len(self.inputs) == 0 and wait_for_inputs:
                    return False
                write_position = self.position(mode_1, 1)
                self.program[write_position] = self.inputs.pop(0)
                self.read_pos += 2
            elif instruction == OUTPUT:
                output = self.read(self.position(mode_1, 1))
                self.outputs.append(output)
                self.read_pos += 2
            elif instruction == ADJUST_RELATIVE:
                self.relative_base += self.program[self.position(mode_1, 1)]
                self.read_pos += 2
            elif instruction in jump_cases.keys():
                (value1, value2) = self.values(mode_1, mode_2)

                self.read_pos = jump_cases[instruction](value1, value2, self.read_pos)
            elif instruction in value_write_cases.keys():
                (value1, value2) = self.values(mode_1, mode_2)
                position3 = self.position(mode_3, 3)
                self.program[position3] = value_write_cases[instruction](value1, value2)
                self.read_pos += 4
            else:
                raise Exception('bad')

    def position(self, mode, lookahead):
        if mode == 0:  # position
            return self.program[self.read_pos + lookahead]
        elif mode == 2:  # relative
            return self.program[self.read_pos + lookahead] + self.relative_base
        else:  # immediate
            return self.read_pos + lookahead

    def values(self, *modes):
        return (self.read(self.position(mode, ix + 1)) for ix, mode in enumerate(modes))

    def read(self, index):
        return self.program[index] if index in self.program else 0
