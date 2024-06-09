
# Algoritmo para debucir si 
# un año es bisiesto o no 

try:
	año = int(input("Ingrese el año: "))

	if año % 4 == 0:
		print("Es un año bisiesto")

	else:
		print("No es un año bisiesto")

except ValueError:
	print("Solo numeros")