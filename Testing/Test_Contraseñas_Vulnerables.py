
from Ruta_Scripts import *
import pytest
from Generador_Claves import claves_seguras
import pandas as pd

# Prueba para validar restricciones de longitud
@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (5, "Longitud mínima 8 y máxima 128."),  # Menor a la longitud mínima
        (150, "Longitud mínima 8 y máxima 128."),  # Mayor a la longitud máxima
    ]
)
def test_claves_seguras_restricciones(input_value, expected_output):
    resultado = claves_seguras(input_value)
    assert resultado == expected_output

# Prueba para asegurar que se genera una contraseña de la longitud esperada
def test_claves_seguras_longitud():
    longitud = 12
    _, clave_generada = claves_seguras(longitud)
    assert len(clave_generada) == longitud

# Prueba para asegurar que las contraseñas generadas son únicas
def test_contraseñas_unicas():
    claves = [claves_seguras(8)[1] for _ in range(10)]
    assert len(set(claves)) == len(claves)  # Las contraseñas deben ser únicas

# Prueba para verificar la comparación de contraseñas en DataFrame
def test_comparacion_contraseñas():
    claves = [claves_seguras(8)[1] for _ in range(10)]
    claves_generadas = [claves_seguras(8)[1] for _ in range(10)]
    comparacion = [i == j for i, j in zip(claves, claves_generadas)]

    df_claves = pd.DataFrame({
        "Claves": claves,
        "Claves Generadas": claves_generadas,
        "Comparación": comparacion
    })

    # Verificar que no todas las contraseñas sean iguales
    assert not all(df_claves["Comparación"])