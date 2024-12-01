
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

import pytest
from unittest.mock import patch
from Año_Bisiesto import es_bisiesto

# Si es bisiesto
@patch("builtins.input", return_value = "2024")
def test_es_bisiesto(mock_input):

	resultado = es_bisiesto()
	assert resultado  == "Es un año bisiesto"

# Si no es bisiesto
@patch("builtins.input", return_value = "2023")
def test_no_es_bisiesto(mock_input):

	resultado = es_bisiesto()
	assert resultado == "No es un año bisiesto"

# Si el valor no es numérico
@patch("builtins.input", return_value = "abc")
def test_entrada_invalida(mock_input):

	resultado = es_bisiesto()
	assert resultado == "Solo números"