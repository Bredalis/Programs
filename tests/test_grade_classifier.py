
from path_setup import *

import pytest
from grade_classifier import classify_grade


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("95", "Excellent, you are very smart!\n"),
        ("60", "You need to improve\n"),
        ("85", "Very good, you are hardworking!\n"),
        ("abc", "Error: Numbers only\n"),
    ],
)
def test_classify_grade(input_value, expected_output, monkeypatch, capsys):
    """Test grade classification with different inputs."""

    # Mock user input
    monkeypatch.setattr("builtins.input", lambda _: input_value)

    classify_grade()

    # Capture printed output
    captured = capsys.readouterr()

    assert captured.out == expected_output
