from solutions import helpers
import numpy as np
from scipy import ndimage

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

enhancement_algorithm = np.array(list(strings[0]), dtype=str) == '#'

input_image = np.array([list(row) for row in strings[2:]], dtype=str) == '#'


def display(img):
    for row in img:
        print("".join(['.' if not el else '#' for el in row]))


def enhance(a):
    val = int(''.join(a.astype('int').astype('str')), 2)
    return enhancement_algorithm[val]


for ix in range(2):
    pad_size = 2
    padded_input = np.pad(
        array=input_image,
        pad_width=pad_size,
        mode='constant',
        constant_values=(enhancement_algorithm[0] and (ix % 2))
    )

    output_image = ndimage.generic_filter(
        input=padded_input,
        function=enhance,
        size=(3, 3),
        mode='constant',
        cval=False
    )

    crop_size = pad_size - 1
    cropped_output = output_image[crop_size:-crop_size, crop_size:-crop_size]

    input_image = cropped_output


print(np.sum(input_image))
