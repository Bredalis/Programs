
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

# Libreria para testing

import pytest
from Numeros_Primos import numeros_primos

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		(4, "4 no es primo"),
		(3, "3 es primo"),
		("abc", "Solo numeros")
	]
)

def test_numeros_primos(input_value, expected_output, monkeypatch, capsys):

	# Simulamos la entrada del usuario
	monkeypatch.setattr("builtins.input", lambda _: input_value)

	# Capturamos la salida
	resultado = numeros_primos()

	# Comprobamos que la salida sea la esperada
	assert resultado == expected_output