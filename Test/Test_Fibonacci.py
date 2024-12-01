
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

# Librerías de testing

import pytest
from Fibonacci import fibonacci

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		(0, 0),
		(1, 1),
		(9, 34)
	]
)

def test_fibonacci(input_value, expected_output):
	resultado = fibonacci(input_value)
	assert resultado == expected_output