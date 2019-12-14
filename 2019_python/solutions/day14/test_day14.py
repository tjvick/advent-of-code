import part1
import part2


class TestDayM:
    def test_part1_scenario0(self):
        assert part1.main('./scratch.txt') == 31

    def test_part1_scenario1(self):
        assert part1.main('./scratch1.txt') == 165

    def test_part1_scenario2(self):
        assert part1.main('./scratch2.txt') == 13312

    def test_part1_scenario3(self):
        assert part1.main('./scratch3.txt') == 180697

    def test_part1_scenario4(self):
        assert part1.main('./scratch4.txt') == 2210736

    def test_part2_scenario2(self):
        assert part2.main('./scratch2.txt') == 82892753

    def test_part2_scenario3(self):
        assert part2.main('./scratch3.txt') == 5586022

    def test_part2_scenario4(self):
        assert part2.main('./scratch4.txt') == 460664



