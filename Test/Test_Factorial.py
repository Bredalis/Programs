
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

# Librerías de testing

import pytest
from Factorial import factorial

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		(0, 1),
		(4, 24),
		(9, 362880)
	]
)

def test_factorial(input_value, expected_output):
	resultado = factorial(input_value)
	assert resultado == expected_output