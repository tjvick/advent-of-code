def missing_number(x):
    full_length = len(x) + 1
    expected_sum = full_length * (full_length + 1) / 2
    return expected_sum - sum(x)


def test_missing_number_returns_a_number():
    x = [3, 4, 6, 2, 1, 7, 9, 5]
    assert missing_number(x) == 8


def test_missing_number_returns_missing_number():
    x = [3, 4, 6, 2, 1, 7, 9, 8]
    assert missing_number(x) == 5

