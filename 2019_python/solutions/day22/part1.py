import re

def deal_into_new_stack(starting_deck):
    return starting_deck[::-1]


def cut(starting_deck, n_cards):
    return starting_deck[n_cards:] + starting_deck[:n_cards]


def deal_increment(starting_deck, increment):
    new_deck = [-1]*len(starting_deck)
    ix = 0
    while starting_deck:
        new_deck[ix] = starting_deck.pop(0)
        ix = (ix + increment) % len(new_deck)

    return new_deck


def shuffle(content, deck_size):
    deck = list(range(deck_size))
    for line in content:
        m_increment = re.match(r"deal with increment (\d+)", line)
        if m_increment:
            increment = int(m_increment.group(1))
            deck = deal_increment(deck, increment)
            continue

        m_deal = re.match(r"deal into new stack", line)
        if m_deal:
            deck = deal_into_new_stack(deck)
            continue

        m_cut = re.match(r"cut (-?\d+)", line)
        if m_cut:
            deck = cut(deck, int(m_cut.group(1)))

    return deck


def main():
    with open('./input.txt', 'r') as f:
        content = [line.strip('\n') for line in f]

    return shuffle(content, 10007).index(2019)


if __name__ == "__main__":
    print(main())
