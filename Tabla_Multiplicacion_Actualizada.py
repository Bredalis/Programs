
print("\nTabla de Multiplicacion")

def tablas_muplicacion(numero):

	tema = "Tabla"

	print(f"\n{tema} {numero}")

	for i in range(0, 11):
		print(f"{i} X {numero} = {i * numero}")

for i in range(0, 11):
	tablas_muplicacion(i)