from part1 import run_program
import part1
import part2


class TestDay9:
    def test_1(self):
        string_program = "1102,34915192,34915192,7,4,7,99,0"
        assert run_program(string_program, []) == [1219070632396864]

    def test_2(self):
        string_program = "104,1125899906842624,99"
        assert run_program(string_program, []) == [1125899906842624]

    def test_3(self):
        string_program = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
        assert run_program(string_program, []) == [
            109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99
        ]

    def test_part1(self):
        assert part1.main() == 2870072642

    def test_part2(self):
        assert part2.main() == 58534

