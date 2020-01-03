import part1
import part2


class TestDay22:
    def test_deal_into_new_stack(self):
        deck = [0, 1, 2, 3, 4, 5, 6]
        assert part1.deal_into_new_stack(deck) == [6, 5, 4, 3, 2, 1, 0]

    def test_cut_positive_3_cards(self):
        deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert part1.cut(deck, 3) == [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]

    def test_cut_negative_4_cards(self):
        deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert part1.cut(deck, -4) == [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]

    def test_deal_with_increment_3(self):
        deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert part1.deal_increment(deck, 3) == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]

    def test_shuffle_1(self):
        instructions = [
            "deal with increment 7",
            "deal into new stack",
            "deal into new stack"
        ]

        new_deck = part1.shuffle(instructions, 10)
        assert " ".join([str(x) for x in new_deck]) == "0 3 6 9 2 5 8 1 4 7"

    def test_shuffle_2(self):
        instructions = [
            "cut 6",
            "deal with increment 7",
            "deal into new stack"
        ]

        new_deck = part1.shuffle(instructions, 10)
        assert " ".join([str(x) for x in new_deck]) == "3 0 7 4 1 8 5 2 9 6"

    def test_shuffle_3(self):
        instructions = [
            "deal into new stack",
            "cut -2",
            "deal with increment 7",
            "cut 8",
            "cut -4",
            "deal with increment 7",
            "cut 3",
            "deal with increment 9",
            "deal with increment 3",
            "cut -1",
        ]

        new_deck = part1.shuffle(instructions, 10)
        assert " ".join([str(x) for x in new_deck]) == "9 2 5 8 1 4 7 0 3 6"