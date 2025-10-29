import pytest
from random import randint
from src.hw6.heap_sort import heap_sort, bubble_sort


def random_arr(lenght):
    arr = [0] * lenght
    for i in range(lenght):
        arr[i] = randint(1, 10**9)
    return arr


TEST_CASES = [
    ([], [], "no elem"),
    ([1], [1], "one elem"),
    ([1, 2, 3], [1, 2, 3], "no need to sort"),
    ([2, 1], [1, 2], "sort two elem"),
    ([1, 3, 2], [1, 2, 3], "sort three elem"),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], "inversion")
]

TEST_CASES_RANDOM_SOFT = [random_arr(randint(1, 30)) for i in range(30)]
TEST_CASES_RANDOM_HARD = [random_arr(randint(1, 10**3)) for i in range(30)]


class TestHeapSort:
    @pytest.mark.parametrize("arr", TEST_CASES_RANDOM_SOFT)
    def test_keep_lenght(arr):
        return len(arr) == len(heap_sort(arr))


    @pytest.mark.parametrize("arr,expected,tats_name", TEST_CASES)
    def test_unit_heap_sort(arr, expected, test_name):
        new_arr = arr[:]
        heap_sort(new_arr)
        assert new_arr == expected


    @pytest.mark.parametrize("arr", TEST_CASES_RANDOM_HARD)
    def test_heap_sort_random(arr):
        assert heap_sort(arr) == bubble_sort(arr)
