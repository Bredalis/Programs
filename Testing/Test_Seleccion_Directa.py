
from Ruta_Scripts import *

# Librería de testing
import pytest
from Seleccion_Directa import seleccion_directa

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		([1, 4, 13, 7, 9, 0.5, 3, 10], [0.5, 1, 3, 4, 7, 9, 10, 13]),
		([1, "b", 13, "a", 3, 10], []),
		([], []),
		(["b", "a"], ['a', 'b']),
		(None, [])
	]
)

def test_seleccion_directa(input_value, expected_output):
	resultado = seleccion_directa(input_value)
	assert resultado == expected_output