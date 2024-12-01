
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

# Librerías de testing

import pytest
from Selection_Sort import selection_sort

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		([], []),
		("", None),
		(["a", "c", "b"], ["a", "b", "c"]),
		([5, 3, 1, 4, 2], [1, 2, 3, 4, 5])
	]
)

def test_selection_sort(input_value, expected_output):
	resultado = selection_sort(input_value)
	assert resultado == expected_output