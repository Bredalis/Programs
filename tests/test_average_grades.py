
from path_setup import *

import pytest
from average_grades import average


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ([56, 70, 88, 88], 76),
        ("None", None),
        ([], "Enter a list of 4 grades"),
        ([100, 50], "Enter a list of 4 grades"),
    ],
)
def test_average(input_value, expected_output):
    """
    Test grade average calculation
    """
    result = average(input_value)
    assert result == expected_output
