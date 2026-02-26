
from path_setup import *

import pytest
from ascii_encoder_decoder import encode_ascii, decode_ascii


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("Hola", "72 111 108 97"),
        ("67", "54 55"),
    ],
)
def test_encode_ascii(input_value, expected_output):
    """Test ASCII encoding"""
    result = encode_ascii(input_value)
    assert result == expected_output


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("32", " "),
        ("72 111 108 97", "Hola"),
        (
            "Hola",
            "Unexpected error: invalid literal for int() with base 10: 'Hola'",
        ),
    ],
)
def test_decode_ascii(input_value, expected_output):
    """Test ASCII decoding"""
    result = decode_ascii(input_value)
    assert result == expected_output
