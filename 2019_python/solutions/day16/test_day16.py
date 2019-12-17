import part1


example_input = "12345678"

class TestDayM:
    # def test_get_scalar_pattern_0(self):
    #     assert part1.get_scalar_pattern(0) == [1, 0, -1, 0]
    #
    # def test_get_scalar_pattern_1(self):
    #     assert part1.get_scalar_pattern(1) == [0, 1, 1, 0, 0, -1, -1, 0]
    #
    # def test_get_scalar_pattern_2(self):
    #     assert part1.get_scalar_pattern(2) == [0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1, 0]
    #
    # def test_get_scalar_pattern_4(self):
    #     assert part1.get_scalar_pattern(4) == [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, 0]
    #
    # def test_run_fft_example_after_1_step(self):
    #     assert part1.run_fft(example_input, 1) == "48226158"
    #
    # def test_run_fft_example_after_2_steps(self):
    #     assert part1.run_fft(example_input, 2) == "34040438"
    #
    # def test_run_fft_example_after_3_steps(self):
    #     assert part1.run_fft(example_input, 3) == "03415518"
    #
    # def test_run_fft_example_after_4_steps(self):
    #     assert part1.run_fft(example_input, 4) == "01029498"
    #
    # def test_run_fft_example2_after_100_steps(self):
    #     assert part1.run_fft("80871224585914546619083218645595", 100)[0:8] == "24176176"

    def test_part2_run_fft_example1_after_1_step(self):
        assert part1.run_fft(example_input, 1) == "48226158"

    def test_part2_run_fft_example1_after_2_steps(self):
        assert part1.run_fft(example_input, 2) == "34040438"

    def test_part2_run_fft_example1_after_3_steps(self):
        assert part1.run_fft(example_input, 3) == "03415518"

    def test_part2_run_fft_example1_after_4_steps(self):
        assert part1.run_fft(example_input, 4) == "01029498"

    def test_part2_run_fft_example2_after_100_steps(self):
        assert part1.run_fft("80871224585914546619083218645595", 100)[0:8] == "24176176"

    def test_part2_run_fft_example3_after_100_steps(self):
        assert part1.run_fft("19617804207202209144916044189917", 100)[0:8] == "73745418"

    def test_part2_run_fft_example4_after_100_steps(self):
        assert part1.run_fft("69317163492948606335995924319873", 100)[0:8] == "52432133"
