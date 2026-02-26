
from path_setup import *

from unittest.mock import patch
from leap_year_checker import is_leap_year


# Test: year is a leap year
@patch("builtins.input", return_value="2024")
def test_is_leap_year(mock_input):
    result = is_leap_year()
    assert result == "It is a leap year"


# Test: year is not a leap year
@patch("builtins.input", return_value="2023")
def test_is_not_leap_year(mock_input):
    result = is_leap_year()
    assert result == "It is not a leap year"


# Test: invalid input
@patch("builtins.input", return_value="abc")
def test_invalid_input(mock_input):
    result = is_leap_year()
    assert result == "Error: Please enter numbers only"
