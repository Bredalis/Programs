
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

# Librerías de testing

import pytest
from Insertion_Sort import insertion_sort

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		([], []),
		([2, 1, 0, 3], [0, 1, 2, 3])
	]
)

def test_insertion_sort(input_value, expected_output):
	resultado = insertion_sort(input_value)
	assert resultado == expected_output