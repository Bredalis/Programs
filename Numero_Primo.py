
# Algoritmo para determinar 
# si un número es primo o no

try:
	numero = int(input("Ingrese el numero: "))

	for i in range(2, numero):
		if numero % i != 0:
			print(f"{numero} es primo")

		else:
			print(f"{numero} no es primo")
		break
	
except ValueError:
	print("Solo numeros")