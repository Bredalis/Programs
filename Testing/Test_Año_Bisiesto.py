
from Ruta_Scripts import *

from unittest.mock import patch
from Año_Bisiesto import es_bisiesto

# Pruebas unitarias

@patch("builtins.input", return_value = "2024")
def test_es_bisiesto(mock_input):
	resultado = es_bisiesto()
	assert resultado  == "Es bisiesto"

@patch("builtins.input", return_value = "2023")
def test_no_es_bisiesto(mock_input):
	resultado = es_bisiesto()
	assert resultado == "No es bisiesto"

@patch("builtins.input", return_value = "abc")
def test_entrada_invalida(mock_input):
	resultado = es_bisiesto()
	assert resultado == "Error: Solo ingrese números"