def min_v2(x):
    current_min = x[0]
    for element in x:
        if element < current_min:
            current_min = element

    return current_min


def test_min_returns_min_value_of_length_1_array():
    x = [0]
    assert min_v2(x) == 0


def test_min_returns_min_value_of_presorted_array():
    x = [1, 5]
    assert min_v2(x) == 1


def test_min_returns_min_value_of_unsorted_array():
    x = [1, 5, 3, 0]
    assert min_v2(x) == 0


def test_min_returns_negative_values():
    x = [-10, -20, -1, 3, 6, 0]
    assert min_v2(x) == -20
