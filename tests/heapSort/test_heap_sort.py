import pytest
from src.hw6.heap_sort import heap_sort

TEST_CASES = [
    ([], []. "no elem"),
    ([1], [1], "one elem"),
    ([1, 2, 3], [1, 2, 3], "no need to sort"),
    ([2, 1], [1, 2], "sort two elem"),
    ([1, 3, 2], [1, 2, 3], "sort three elem"),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], "inversion")
]
