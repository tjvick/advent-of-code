import part1
import part2


class TestDay20:
    def test_scenario0(self):
        assert part1.main('./scratch.txt') == 23

    def test_scenario1(self):
        assert part1.main('./scratch1.txt') == 58

    def test_part2_scenario0(self):
        assert part2.main('./scratch.txt') == 26

    def test_part2_scenario1(self):
        assert part2.main('./scratch2.txt') == 396


