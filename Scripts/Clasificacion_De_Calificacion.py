
print("Clasificador de notas con valor de 100 puntos")

while(True):

	try:
		nota = int(input("Nota: "))

		if nota >= 90 and nota <= 100:
			print("¡Excelente, eres inteligente!")

		elif nota <= 70:
			print("Tienes que mejorar")

		elif nota < 90 and nota > 70 and nota < 100:
			print("¡Muy Bien, eres aplicado!")

		break

	except ValueError:
		print("Solo Numeros")	