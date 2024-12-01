
from Ruta_Scripts import *

# Librería de testing
import pytest
from Generador_Claves import claves_seguras

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		(5, "Longitud mínima 8 y máxima 128."),
		(1000, "Longitud mínima 8 y máxima 128."),
		("a", "Error inesperado: '<' not supported between instances of 'str' and 'int'")
	]
)

def test_claves_seguras(input_value, expected_output):
	resultado = claves_seguras(input_value)
	assert resultado == expected_output