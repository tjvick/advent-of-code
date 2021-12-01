def deduplicate(array):
    current_length = len(array)
    previous = array[0]
    ix = 1
    while ix < current_length:
        if array[ix] == previous:
            array.pop(ix)
            current_length += -1
        else:
            ix += 1


def test_deduplicate_does_not_change_a_unique_set():
    x = [1, 2, 3]
    deduplicate(x)
    assert x == [1, 2, 3]


def test_deduplicate_removes_duplicates_in_place():
    x = [1, 1]
    deduplicate(x)
    assert x == [1]