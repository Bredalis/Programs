
# Algoritmo para deducir si 
# un año es bisiesto o no 

def es_bisiesto():
	try:
<<<<<<< HEAD
		anio = int(input("Ingrese el año: "))
		return "Es bisiesto" if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) else "No es bisiesto"

	except ValueError:
		return "Error: Solo ingrese números"

	except Exception as e:
		print(f"Error inesperado: {e}")
=======
		año = int(input("Ingrese el año: "))

		if año % 4 == 0:
			return "Es un año bisiesto"

		else:
			return "No es un año bisiesto"

	except ValueError:
		return "Solo números"
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
