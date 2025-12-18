import pytest
from src.hw6.heap_sort import rise_elem, fall_elem

TEST_CASES_RISE = [
    ([], [], "empty list"),
    ([1], [1], "one element"),
    ([3, 2, 1], [3, 2, 1], "already max heap"),
    ([2, 1, 3], [3, 1, 2], "rise largest, high is two"),
    ([6, 5, 4, 3, 2, 1, 7], [7, 5, 6, 3, 2, 1, 4], "rise largest, high is three"),
    ([4, 1, 2, 3], [4, 3, 2, 1], "rise not largest"),
]

TEST_CASES_FALL = [
    ([], [], "empty list"),
    ([1], [1], "one element"),
    ([3, 2, 1], [3, 2, 1], "already in the right place"),
    ([1, 3, 2], [3, 1, 2], "swap with left child"),
    ([1, 2, 3], [3, 2, 1], "swap with right child"),
    ([2, 1], [2, 1], "haven't right child, don't swap"),
    ([1, 2], [2, 1], "haven't right child, swap"),
    ([1, 5, 4, 3, 2], [5, 3, 4, 1, 2], "fall to the very bottom, high is three"),
    ([3, 5, 4, 1, 2], [5, 3, 4, 1, 2], "fall not to the very bottom, high is three"),
]


class TestHeapSortUtils:
    """Unit-tests for heap functions"""

    @pytest.mark.parametrize("arr,expected,test_name", TEST_CASES_RISE)
    def test_rise_elem(self, arr, expected, test_name):
        new_arr = arr[:]
        rise_elem(new_arr, len(arr) - 1)
        assert new_arr == expected

    @pytest.mark.parametrize("arr,expected,test_name", TEST_CASES_FALL)
    def test_fall_elem(self, arr, expected, test_name):
        new_arr = arr[:]
        fall_elem(new_arr, len(arr))
        assert new_arr == expected
