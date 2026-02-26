
from path_setup import *

import pytest
from selection_sort import selection_sort


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ([5, 3, 1, 4, 2], [1, 2, 3, 4, 5]),
        ([], []),
        ("", None),
        (["a", "c", "b"], ["a", "b", "c"]),
    ],
)
def test_selection_sort(input_value, expected_output):
    """
    Test selection sort algorithm
    """
    result = selection_sort(input_value)
    assert result == expected_output
