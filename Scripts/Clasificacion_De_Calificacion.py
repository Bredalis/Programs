
print("Clasificador de notas con valor de 100 puntos")

def calificacion_puntuacion():
	try:
		nota = int(input("Nota final: "))

		if nota >= 90 and nota <= 100:
			print("¡Excelente, eres inteligente!")

		elif nota <= 70:
			print("Tienes que mejorar")

		elif nota < 90 and nota > 70 and nota < 100:
			print("¡Muy Bien, eres aplicado!")

	except ValueError:
		print("Error: Solo números")

	except Exception as e:
		print(f"Error inesperado: {e}")