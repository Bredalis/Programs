
from Ruta_Scripts import *

# Librería de testing
import pytest
from Linear_Search import linear_search

# Casos de prueba
@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		([], 2, None),
		([2, 1, 0, 3], 3, 3),
		([2, 1, 0, 3], "a", None),
		([2, 1, 0, "a"], "a", "a"),
		([2, 1, 0, 3], 100, None)
	]
)

def test_linear_search(input_x, input_y, expected):
	resultado = linear_search(input_x, input_y)
	assert resultado == expected