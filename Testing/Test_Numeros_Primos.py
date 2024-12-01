
from Ruta_Scripts import *

# Librería para testing
import pytest
from Numeros_Primos import numeros_primos

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		(4, "No es primo"),
		(3, "Es primo"),
		("abc", "Error: Solo números")
	]
)

def test_numeros_primos(input_value, expected_output, monkeypatch, capsys):
	# Simular la entrada del usuario
	monkeypatch.setattr("builtins.input", lambda _: input_value)

	# Capturar la salida
	resultado = numeros_primos()
	assert resultado == expected_output