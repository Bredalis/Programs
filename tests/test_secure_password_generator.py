
from path_setup import *

import pytest

from secure_password_generator import generate_secure_password


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (5, "Minimum length is 8 and maximum is 128."),
        (1000, "Minimum length is 8 and maximum is 128."),
        ("a", "Unexpected error: Length must be an integer."),
    ],
)
def test_generate_secure_password(input_value, expected_output):
    """
    Test secure password generation with invalid inputs.
    """
    result = generate_secure_password(input_value)
    assert result == expected_output
