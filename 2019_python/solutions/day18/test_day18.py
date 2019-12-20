import part1


class TestDayM:
    def test_scenario0(self):
        assert part1.main('./scratch.txt') == 8

    def test_scenario1(self):
        assert part1.main('./scratch1.txt') == 86

    def test_scenario2(self):
        assert part1.main('./scratch2.txt') == 132

    def test_scenario3(self):
        assert part1.main('./scratch3.txt') == 136

    def test_scenario4(self):
        assert part1.main('./scratch4.txt') == 81

