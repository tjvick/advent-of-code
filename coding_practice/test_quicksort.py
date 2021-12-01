def partition(array, low, high):
    fence = array[low]

    ix_fence = low
    for ix in range(low, high):
        # if element is less than the fence value
        if array[ix] < fence:
            # move the fence one to the right
            ix_fence += 1
            # move the element to the new fence location.  This will eventually result in all elements to the left of
            # the fence being less than the fence.
            array[ix_fence], array[ix] = array[ix], array[ix_fence]

    # move the fence to its final location
    # move the element at the fence location (which is lower than the fence value) to the beginning
    array[ix_fence], array[low] = array[low], array[ix_fence]
    return ix_fence


def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)

        quick_sort(array, low, p)
        quick_sort(array, p + 1, high)


def quicksort(array):
    quick_sort(array, 0, len(array))

    return array


def test_quicksort_returns_empty_array_when_provided():
    result = quicksort([])
    assert result == []


def test_quicksort_returns_presorted_array_unchanged():
    assert quicksort([1, 2, 3]) == [1, 2, 3]


def test_quicksort_sorts_length_2_array():
    assert quicksort([3, 1]) == [1, 3]


def test_quicksort_sorts_length_3_array():
    assert quicksort([3, 5, 1]) == [1, 3, 5]


def test_quicksort_sorts_length_11_array():
    assert quicksort([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1, 12]) == [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 12]
