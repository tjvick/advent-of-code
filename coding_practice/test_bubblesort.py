def bubblesort(array):
    n_pairs_to_consider = len(array) - 1
    unsorted = True
    while unsorted:
        unsorted = False
        for ix0 in range(n_pairs_to_consider):
            ix1 = ix0 + 1
            if array[ix0] > array[ix1]:
                array[ix0], array[ix1] = array[ix1], array[ix0]
                unsorted = True

        n_pairs_to_consider += -1

    return array



def test_bubblesort_returns_length_one_array_unchanged():
    assert bubblesort([0]) == [0]


def test_bubblesort_returns_length_two_presorted_array_unchanged():
    assert bubblesort([1, 2]) == [1, 2]


def test_bubblesort_swaps_two_elements_in_length_two_unsorted_array():
    assert bubblesort([2, 1]) == [1, 2]


def test_bubblesort_sorts_a_length_3_reversed_array():
    assert bubblesort([3, 2, 1]) == [1, 2, 3]


def test_bubblesort_sorts_a_length_10_unordered_array():
    assert bubblesort([5, 3, 7, 10, 2, 4, 9, 1, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]