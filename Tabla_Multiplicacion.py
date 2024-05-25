"""
Programa que muestra 
la tabla del 1 - 100 
del numero ingresado 
por el usuario
"""

print("Tabla de Multiplicacion")

while(True):

	# Obtener solo numero

	try:
		factor_1 = int(input("Introduce el numero para la tabla: "))

		# Bucle que crea la tabla

		for factor_2 in range(1, 101):
			multiplicacion = factor_1 * factor_2
			print(f"{factor_1} X {factor_2} = {multiplicacion}")

		break

	except ValueError:
		print("Solo numeros")