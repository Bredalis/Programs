
from Ruta_Scripts import *

# Librería de testing
import pytest
from Promedio_De_Notas import promedio

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		([56, 70, 88, 88], 76),
		("None", None),
		([], "Ingrese una lista de 4 notas"),
		([100, 50], "Ingrese una lista de 4 notas")
	]
)

def test_promedio(input_value, expected_output):
	resultado = promedio(input_value)
	assert resultado == expected_output