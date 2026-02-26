
from path_setup import *

# Testing library
import pytest
from morse_translator import translate_to_morse

# Test cases


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("Hola, Mundo", ".... --- .-.. .-   -- ..- -. -.. ---"),
        ("Python", ".--. -.-- - .... --- -."),
        ("Bredalis", "-... .-. . -.. .- .-.. .. ...")
    ]
)
def test_translate_to_morse(input_value, expected_output):
    result = translate_to_morse(input_value)
    assert result == expected_output
