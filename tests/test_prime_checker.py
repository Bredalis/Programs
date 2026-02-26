
from path_setup import *

import pytest
from prime_checker import is_prime


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (4, "Not prime"),
        (3, "Prime"),
        ("abc", "Error: Numbers only"),
    ],
)
def test_is_prime(input_value, expected_output, monkeypatch):
    """
    Test the prime number function with simulated user input
    """
    monkeypatch.setattr("builtins.input", lambda _: input_value)

    result = is_prime()
    assert result == expected_output
