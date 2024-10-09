
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

# Librerías de testing

import pytest
from Codigo_Morce import traduccion

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		("Hola, Mundo", ".... --- .-.. .-   -- ..- -. -.. ---"),
		("Python", ".--. -.-- - .... --- -."),
		("Bredalis", "-... .-. . -.. .- .-.. .. ...")
	]
)

def test_traduccion(input_value, expected_output):
	resultado = traduccion(input_value)
	assert resultado == expected_output