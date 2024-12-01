
from Ruta_Scripts import *

import pytest
from Clasificacion_De_Calificacion import calificacion_puntuacion

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		("95", "¡Excelente, eres inteligente!\n"),
		("60", "Tienes que mejorar\n"),
		("85", "¡Muy Bien, eres aplicado!\n"),
		("abc", "Error: Solo números\n")
	]
)

def test_calificacion_puntuacion(input_value, expected_output, monkeypatch, capsys):
	# Simular de la entrada del usuario
	monkeypatch.setattr("builtins.input", lambda _: input_value)
	calificacion_puntuacion()

	# Capturar salida
	captured = capsys.readouterr()
	assert captured.out == expected_output