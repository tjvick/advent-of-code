import part2


class TestDayM:
    def test_0(self):
        pattern0 = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1]
        assert part2.apply_rules(pattern0) == 3

    def test_1(self):
        pattern = [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        assert part2.apply_rules(pattern) == 4

    def test_2(self):
        pattern = [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1]
        assert part2.apply_rules(pattern) == 4

    def test_3(self):
        pattern = [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
        assert part2.apply_rules(pattern) == 4

    def test_4(self):
        pattern = [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
        assert part2.apply_rules(pattern) == 4
