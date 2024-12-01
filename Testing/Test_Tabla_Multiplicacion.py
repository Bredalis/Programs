
from Ruta_Scripts import *

# Librería de testing
import pytest
from Tabla_Multiplicacion import tabla_muplicacion

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		(0, [f"0 X {i} = {0 * i}" for i in range(11)]),
		(5, [f"5 X {i} = {5 * i}" for i in range(11)]),
		(10, [f"10 X {i} = {10 * i}" for i in range(11)]),
		(15, [f"15 X {i} = {15 * i}" for i in range(11)]),
		(20, [f"20 X {i} = {20 * i}" for i in range(11)])
	]
)

def test_tabla_muplicacion(input_value, expected_output):
	resultado = tabla_muplicacion(input_value)
	assert resultado == expected_output