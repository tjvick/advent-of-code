import part1
import part2


class TestDay7:
    def test_main_part1(self):
        assert part1.main() == 206580

    def test_main_part2(self):
        assert part2.main() == 2299406