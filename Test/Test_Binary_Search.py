
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

import pytest
from Binary_Search import binary_search

# Parametros
@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		([], 2, "Lista vacía"),
		([1, 2, 3, 4], "", "El número no esta"),
		([1, 2, 3, 4], 10, "El número no esta"),
		([1, 2, 3, 4, 5], 3, "3 esta en el centro"),
		([1, 2, 3, 4], 1, "1 esta en la izquierda"),
		([1, 2, 3, 4], 4, "4 esta en la derecha")
	]
)

def test_binary_search(input_x, input_y, expected):
	resultado = binary_search(input_x, input_y)
	assert resultado == expected