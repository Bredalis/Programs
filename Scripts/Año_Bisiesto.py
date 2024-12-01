
# Algoritmo para deducir si 
# un año es bisiesto o no 

def es_bisiesto():
	try:
		anio = int(input("Ingrese el año: "))
		return "Es bisiesto" if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) else "No es bisiesto"

	except ValueError:
		return "Error: Solo ingrese números"

	except Exception as e:
		print(f"Error inesperado: {e}")