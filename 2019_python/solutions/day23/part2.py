import sys
sys.path.append('..')
from shared.intcode import IntCode


class NetworkComputers:
    def __init__(self, program, address, queue):
        self.p = IntCode(program, [address])
        self.input_queue = []
        self.queue = queue

    def run(self):
        if len(self.input_queue):
            self.p.inputs += self.input_queue
            self.input_queue = []
        else:
            self.p.inputs += [-1]

        # print('inputs', self.p.inputs)
        done = self.p.run(True)
        if self.p.outputs:
            # print('outputs', self.p.outputs)
            self.queue.extend(self.p.outputs)
            self.p.outputs = []

        return done

    def receive(self, packet):
        self.input_queue.append(packet[0])
        self.input_queue.append(packet[1])


def do_the_thing(content):
    program = list(map(lambda x: int(x), content.split(',')))

    computers = []
    queue = []
    for ix in range(50):
        c = NetworkComputers(program, ix, queue)
        computers.append(c)

    cycles = 0
    idle = False
    NAT_packet = []
    NAT_set = set()
    while True:
        for ix in range(50):
            # print('ix', ix)
            done = computers[ix].run()
            # print('queue', queue)

        if len(queue) == 0:
            # print('IDLE!')
            idle = True

        for ix in range(0, len(queue), 3):
            computer_address = queue.pop(0)
            packet = [queue.pop(0) for _ in range(2)]
            if computer_address == 255:
                NAT_packet = packet
            else:
                computers[computer_address].receive(packet)

        if done:
            break

        if idle:
            # print("NAT_packet", NAT_packet)
            computers[0].receive(NAT_packet)
            idle = False

            if NAT_packet[1] in NAT_set:
                print('REPEAT:', NAT_packet[1])
                return NAT_packet[1]
            NAT_set.add(NAT_packet[1])

        if cycles >= 1000:
            break

        cycles += 1

    return None


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            content = line.strip('\n')

    return do_the_thing(content)


if __name__ == "__main__":
    print(main())
