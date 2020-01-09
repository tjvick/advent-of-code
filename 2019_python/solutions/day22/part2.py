import re


def compute_linear_coeffecients_for_shuffle(instructions, deck_size):
    a = 1
    b = 0
    for line in instructions[::-1]:
        m_increment = re.match(r"deal with increment (\d+)", line)
        if m_increment:
            increment = int(m_increment.group(1))
            mod_inv = pow(increment, deck_size-2, deck_size)
            a = (a * mod_inv) % deck_size
            b = (b * mod_inv) % deck_size
            continue

        m_deal = re.match(r"deal into new stack", line)
        if m_deal:
            a = -a
            b = deck_size - b - 1
            continue

        m_cut = re.match(r"cut (-?\d+)", line)
        if m_cut:
            increment = int(m_cut.group(1))
            a = a
            b = (b + increment) % deck_size

    return a, b


def raise_polynomial_to_power(a, b, power, mod_limit):
    a = a % mod_limit
    b = b % mod_limit
    if power == 0:
        return 1, 0
    elif power % 2 == 0:
        return raise_polynomial_to_power(a**2, (a*b + b), power/2, mod_limit)
    elif power % 3 == 0:
        return raise_polynomial_to_power(a**3, a**2*b + a*b + b, power/3, mod_limit)
    else:
        c, d = raise_polynomial_to_power(a, b, power-1, mod_limit)
        return (a*c) % mod_limit, (a*d + b) % mod_limit


def main():
    with open('./input.txt', 'r') as f:
        content = [line.strip('\n') for line in f]

    deck_size = 119315717514047
    repeats = 101741582076661
    ending_position = 2020

    a, b = compute_linear_coeffecients_for_shuffle(content, deck_size)
    c, d = raise_polynomial_to_power(a, b, repeats, deck_size)

    return (c * ending_position + d) % deck_size


if __name__ == "__main__":
    print(main())
