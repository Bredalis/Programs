
def conversion():

	print("Este es un programa capas de convertir de una temperatura a otra")

	conversiones = ["C a K", "C a F", "K a C", "K a F", "F a C", "F a K"]

	print(f"Estas son las conversiones: {conversiones}")

	eleccion = int(input("Ingrese el tipo de conversion que desea (Por numeros del 0 al 5): "))
	numero = int(input("Ingrese el numero que quiere convertir: "))

	if eleccion == 0:
		print(f"Celsius a Kelvin = {numero + 273.15} ")

	elif eleccion == 1:
		print(f"Celsius a Fahrenheit = {(numero * 9 / 5) + 32}")

	elif eleccion == 2:
		print(f"Kelvin a Celsius = {numero - 273.15}")

	elif eleccion == 3:
		print(f"Kelvin a Fahrenheit = {(numero - 273.15) * 9 / 5 + 32}")

	elif eleccion == 4:
		print(f"Fahrenheit a Celsius = {(numero - 32) * 5 / 9}")

	elif eleccion == 5:
		print(f"Fahrenheit a Kelvin = {(numero - 32) * 5 / 9 + 273.15}")

conversion()