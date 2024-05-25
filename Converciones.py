
from math import floor

valores = [0.018, 54.88, 0.90, 1.11, 60.65, 0.016]
divizas = ["pesos", "dolares", "dolares", "euros", "euros", "pesos"]
divizas_2 = ["dolares", "pesos", "euros", "dolares", "pesos", "euros"]

def conversiones(valor):

	for i in range(0, len(valores)):
		print(f"Por {valor} {divizas[i]}, tenemos {floor(valor * valores[i])} {divizas_2[i]}")

conversiones(100)