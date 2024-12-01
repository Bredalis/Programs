
from Ruta_Scripts import *

# Librería de testing
import pytest
from Codificacion_Ascii import codificar, decodificar

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		("Hola", "72 111 108 97"),
		("67", "54 55")
	]
)

def test_codificar(input_value, expected_output):
	resultado = codificar(input_value)
	assert resultado == expected_output

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		("32", " "),
		("72 111 108 97", "Hola"),
		("Hola", "Error inesperado: invalid literal for int() with base 10: 'Hola'")
	]
)

def test_decodificar(input_value, expected_output):
	resultado = decodificar(input_value)
	assert resultado == expected_output