
"""
Programa que evalúa si una contraseña es fácil de
generar, lo que puede hacerla vulnerable.
"""

from Generador_Claves import claves_seguras
import pandas as pd

# Lista para almacenar las contraseñas generadas
claves = [claves_seguras(8)[1] for i in range(10)]
claves_generadas = [claves_seguras(8)[1] for j in range(10)]
comparacion = [i == j for i, j in zip(claves, claves_generadas)]

df_claves = pd.DataFrame({
	"Claves": claves,
	"Claves Generadas": claves_generadas,
	"Comparación": comparacion
})

print(df_claves)