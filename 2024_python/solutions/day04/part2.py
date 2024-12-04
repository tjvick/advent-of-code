from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

data = helpers.read_as_2d_array_of_characters(filepath)

window_size = (3, 3)
sliding_view = np.lib.stride_tricks.sliding_window_view(data, window_size)

xmask = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=bool)

xmas_options = [
    np.array(['M','M','A','S','S']),
    np.array(['M','S','A','M','S']),
    np.array(['S','M','A','S','M']),
    np.array(['S','S','A','M','M'])
]

xmas_count = 0
for irow in range(sliding_view.shape[0]):
    for icol in range(sliding_view.shape[1]):
        current_view = sliding_view[irow, icol]
        masked_view = np.ma.masked_array(current_view, xmask)
        compressed_view = masked_view.compressed()

        for xmas_option in xmas_options:
            comparison = compressed_view == xmas_option
            if np.all(comparison):
                is_xmas = True
                xmas_count += 1
                break

print(xmas_count)