import re


def pickup_increment(starting_deck, increment):
    new_deck = []
    ix = 0
    while len(new_deck) < len(starting_deck):
        new_deck.append(starting_deck[ix])
        ix = (ix + increment) % len(starting_deck)

    return new_deck


def position_before_deal_increment(deck_size, increment, starting_position):
    ix = 0
    while True:
        if (increment*ix) % deck_size == starting_position:
            return ix
        ix += 1


def position_before_cut(deck_size, n_cards, starting_position):
    return (starting_position + n_cards) % deck_size


def position_before_deal_into_new_stack(deck_size, starting_position):
    return deck_size - starting_position - 1


def position_before_shuffle(instructions, deck_size, ix):
    for line in instructions[::-1]:
        m_increment = re.match(r"deal with increment (\d+)", line)
        if m_increment:
            increment = int(m_increment.group(1))
            ix = position_before_deal_increment(deck_size, increment, ix)
            continue

        m_deal = re.match(r"deal into new stack", line)
        if m_deal:
            ix = position_before_deal_into_new_stack(deck_size, ix)
            continue

        m_cut = re.match(r"cut (-?\d+)", line)
        if m_cut:
            ix = position_before_cut(deck_size, int(m_cut.group(1)), ix)

    return ix


def main():
    with open('./input.txt', 'r') as f:
        content = [line.strip('\n') for line in f]

    deck_size = 119315717514047
    return position_before_shuffle(content, deck_size, 2020)


if __name__ == "__main__":
    print(main())
