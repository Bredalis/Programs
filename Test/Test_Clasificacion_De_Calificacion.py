
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

import pytest
from Clasificacion_De_Calificacion import calificacion_puntuacion

# Casos de prueba
@pytest.mark.parametrize(
	"input_value, expected_output",
	[
		("95", "¡Excelente, eres inteligente!\n"),
		("60", "Tienes que mejorar\n"),
		("85", "¡Muy Bien, eres aplicado!\n"),
		("abc", "Solo Numeros\n")
	]
)

def test_calificacion_puntuacion(input_value, expected_output, monkeypatch, capsys):

	# Simulamos la entrada del usuario
	monkeypatch.setattr("builtins.input", lambda _: input_value)

	# Llamamos a la función
	calificacion_puntuacion()

	# Capturamos la salida
	captured = capsys.readouterr()

	# Comprobamos que la salida sea la esperada
	assert captured.out == expected_output