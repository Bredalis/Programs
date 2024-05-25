
# Algoritmo para 
# entrar a la universidad

pregunta = input("¿Quieres entrar a la universidad?: ")

if pregunta.lower() == "si":
	print("\nDebes cumplir estos requisitos:")
	formulario = input("¿Llenaste el formulario?: ")
	transcripciones = input("¿Hiciste tus transcripciones académicas?: ")
	recomendaciones = input("¿Alguna carta de recomendación?: ")

	if formulario.lower() == "si" and transcripciones.lower() == "si" and recomendaciones.lower():
		print("Estas adentro. Has cumplido con todos los requisitos")

	else:
		print("Necesitas cumplir con todos los requisitos")

else:
	print("No entraras a la universidad")