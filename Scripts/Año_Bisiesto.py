
# Algoritmo para deducir si 
# un año es bisiesto o no 

def es_bisiesto():
	try:
		año = int(input("Ingrese el año: "))

		if año % 4 == 0:
			return "Es un año bisiesto"

		else:
			return "No es un año bisiesto"

	except ValueError:
		return "Solo números"