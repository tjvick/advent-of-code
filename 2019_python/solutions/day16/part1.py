import numpy as np


def get_scalar_pattern(ix_element):
    base_pattern = (0, 1, 0, -1)
    new_pattern = [item for scalar in base_pattern for item in (scalar, )*(ix_element+1)]
    return list(new_pattern[1:]) + [new_pattern[0]]


def run_fft_once(input_elements):
    output_elements = input_elements[:]
    for ix, _ in enumerate(input_elements):
        scalar_pattern = get_scalar_pattern(ix)
        scalar_array = [scalar_pattern[iy % len(scalar_pattern)] for iy in range(len(input_elements))]

        m = np.multiply(input_elements, scalar_array)
        s = sum(m)
        ones_digit = abs(sum(m)) % 10
        output_elements[ix] = ones_digit

    return output_elements


def run_fft(input_signal, n_steps):
    input_elements = list(map(lambda x: int(x), input_signal))
    for ix_step in range(n_steps):
        print('ix_step', ix_step)
        input_elements = run_fft_once(input_elements)

    return ''.join(map(lambda x: str(x), input_elements))


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            input_signal = line.strip('\n')

    return run_fft(input_signal, 100)


if __name__ == "__main__":
    print(main())
