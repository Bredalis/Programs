
from path_setup import *

import pytest
from binary_search import binary_search


# Test cases
@pytest.mark.parametrize(
    "input_numbers, input_target, expected",
    [
        ([], 2, "Empty list"),
        ([1, 2, 3, 4], "", "The number is not in the list"),
        ([1, 2, 3, 4], 10, "The number is not in the list"),
        ([1, 2, 3, 4, 5], 3, "3 is in the center"),
        ([1, 2, 3, 4], 1, "1 is on the left"),
        ([1, 2, 3, 4], 4, "4 is on the right"),
    ],
)
def test_binary_search(input_numbers, input_target, expected):
    result = binary_search(input_numbers, input_target)
    assert result == expected
