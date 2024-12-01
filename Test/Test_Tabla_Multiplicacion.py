
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

# Librerías de testing

import pytest
from Tabla_Multiplicacion import tablas_muplicacion

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		(0, [f"{i} X 0 = {i * 0}" for i in range(11)]),
		(5, [f"{i} X 5 = {i * 5}" for i in range(11)]),
		(10, [f"{i} X 10 = {i * 10}" for i in range(11)]),
		(15, [f"{i} X 15 = {i * 15}" for i in range(11)]),
		(20, [f"{i} X 20 = {i * 20}" for i in range(11)])
	]
)

def test_tablas_muplicacion(input_value, expected_output):
	resultado = tablas_muplicacion(input_value)
	assert resultado == expected_output