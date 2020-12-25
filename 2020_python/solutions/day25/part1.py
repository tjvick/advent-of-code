import numpy as np

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

cpk = int(file_contents[0])
dpk = int(file_contents[1])
print(cpk)
print(dpk)

# cpk = 5764801
# dpk = 17807724

divisor = 20201227

def transform_subject_number(subject_number, loop_size):
    value = 1
    for ix in range(loop_size):
        value *= subject_number
        value = np.remainder(value, divisor)

    return value


def find_loop_size(public_key):
    value = 1
    ix = 0
    while value != public_key:
        value *= 7
        value = np.remainder(value, divisor)
        ix += 1

    return ix

card_loop_size = find_loop_size(cpk)
door_loop_size = find_loop_size(dpk)

print('card_loop_size', card_loop_size)
print('door_loop_size', door_loop_size)


answer = transform_subject_number(dpk, card_loop_size)
print('answer', answer)
answer = transform_subject_number(cpk, door_loop_size)
print('answer', answer)
