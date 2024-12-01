
from Ruta_Scripts import *

# Librería para testing
import pytest
from Operaciones_Conjuntos import producto_cartesiano, relacion_binaria

# Parámetros
@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		({4, 5, 8}, {}, []),
		(set(), set(), []),
		(None, {}, None)		
	]
)

def test_producto_cartesiano(input_x, input_y, expected):
	resultado = producto_cartesiano(input_x, input_y)
	assert resultado == expected

# Parámetros
@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		([(1, 'a'), (3, 'b'), (5, 'c')], lambda x: x[0] > 2, [(3, 'b'), (5, 'c')]),
		([], lambda x: x[0] > 2, []),
		(None, lambda x: x[0] > 3, None)
	]
)

def test_relacion_binaria(input_x, input_y, expected):
	resultado = relacion_binaria(input_x, input_y)
	assert resultado == expected