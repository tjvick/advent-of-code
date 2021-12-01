def pair_sum(array, total):
    sorted_array = sorted(array)

    ix_low = 0
    ix_high = len(array) - 1

    matching_pairs = []
    while ix_low < ix_high:
        current_sum = sorted_array[ix_low] + sorted_array[ix_high]
        if current_sum == total:
            matching_pairs.append((sorted_array[ix_low], sorted_array[ix_high]))
            ix_high += -1
            ix_low += 1
        elif current_sum > total:
            ix_high += -1
        elif current_sum < total:
            ix_low += 1

    return matching_pairs


def test_pair_sum_returns_only_pair():
    x = [5, 10]
    assert (5, 10) in pair_sum(x, 15)


def test_pair_sum_returns_empty_array_when_no_pairs_exist():
    x = [6, 10]
    assert pair_sum(x, 15) == []


def test_pair_sum_finds_single_matching_pair():
    x = [1, 5, 10, 7, 9]
    assert (5, 10) in pair_sum(x, 15)
    assert len(pair_sum(x, 15)) == 1


def test_pair_sum_finds_multiple_mathing_pairs():
    x = [1, 5, 10, 6, 9]
    assert (5, 10) in pair_sum(x, 15)
    assert (6, 9) in pair_sum(x, 15)
    assert len(pair_sum(x, 15)) == 2


def test_pair_sum_finds_multiple_mathing_pairs_with_duplicates():
    x = [1, 5, 10, 6, 9, 5, 10, 10]
    result = pair_sum(x, 15)
    assert len(result) == 3
    assert (5, 10) in result
    result.remove((5, 10))
    assert (5, 10) in result
    assert (6, 9) in result
