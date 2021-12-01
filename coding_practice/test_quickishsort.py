def quickishsort(array):
    if len(array) == 0:
        return []

    fence_value = array[0]

    lowers = []
    highers = []
    on_fence = []
    for element in array:
        if element > fence_value:
            highers.append(element)
        elif element < fence_value:
            lowers.append(element)
        else:
            on_fence.append(element)

    answer = quickishsort(lowers) + on_fence + quickishsort(highers)
    return answer


def test_quicksort_returns_empty_array_when_provided():
    result = quickishsort([])
    assert result == []


def test_quicksort_returns_presorted_array_unchanged():
    x = [1, 2, 3]
    result = quickishsort(x)
    assert result == x


def test_quicksort_sorts_length_2_array():
    x = [3, 1]
    result = quickishsort(x)
    assert result == [1, 3]


def test_quicksort_sorts_length_3_array():
    assert quickishsort([3, 5, 1]) == [1, 3, 5]


def test_quicksort_sorts_length_11_array():
    assert quickishsort([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1, 12]) == [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 12]