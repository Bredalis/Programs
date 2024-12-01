
print("Clasificador de notas con valor de 100 puntos")

def calificacion_puntuacion():
<<<<<<< HEAD
	try:
		nota = int(input("Nota final: "))
=======

	try:
		nota = int(input("Nota: "))
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

		if nota >= 90 and nota <= 100:
			print("¡Excelente, eres inteligente!")

		elif nota <= 70:
			print("Tienes que mejorar")

		elif nota < 90 and nota > 70 and nota < 100:
			print("¡Muy Bien, eres aplicado!")

	except ValueError:
<<<<<<< HEAD
		print("Error: Solo números")

	except Exception as e:
		print(f"Error inesperado: {e}")
=======
		print("Solo Numeros")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
