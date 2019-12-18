import numpy as np


def run_fft_once(input_elements):
    input_elements_flipped = np.flip(input_elements)
    output_elements_flipped = np.cumsum(input_elements_flipped) % 10
    return np.flip(output_elements_flipped)


def run_fft(input_signal, n_steps, n_repeats=1):
    signal_index = int(input_signal[0:7])

    input_signal_repeated = input_signal*n_repeats
    input_signal_chopped = input_signal_repeated[signal_index:]

    input_elements = np.array(list(map(lambda x: int(x), input_signal_chopped)))
    for ix_step in range(n_steps):
        print('ix_step', ix_step)
        input_elements = run_fft_once(input_elements)

    return ''.join(map(lambda x: str(x), input_elements[0:8]))


def main():
    with open('./input.txt', 'r') as f:
        for line in f:
            input_signal = line.strip('\n')

    return run_fft(input_signal, 100, 10000)


if __name__ == "__main__":
    print(main())
