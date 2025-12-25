import pytest
from src.hw11.graph import Graph


# start dfs from first vertex
TEST_CASES = [
    ({}, [], "empty"),

    ({1: []}, [1],\
    "one elem"),

    ({1: [2], 2: []},\
    [1, 2], "two elem"),

    ({1: [2], 2: [3], 3: [1]},\
    [1, 2, 3], "cycle"),

    ({1: [2], 2: [3], 3: [], 4: []},
    [1, 2, 3], "not visit isolated"),

    ({1: [], 2: [3], 3: [2]},
    [1], "isolated")
]


@pytest.mark.parametrize("dct,expected,test_name", TEST_CASES)
def test_dfs(dct, expected, test_name):
    test_graph = Graph(dct)
    dfs_order = test_graph.dfs_order(1)
    assert dfs_order == expected
