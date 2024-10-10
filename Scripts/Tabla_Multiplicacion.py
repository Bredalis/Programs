
print("\nTabla de Multiplicacion")

def tablas_muplicacion(numero: int):

	resultado = []
	print(f"\n{"Tabla"} {numero}")

	for i in range(0, 11):
		resultado.append(f"{i} X {numero} = {i * numero}")

	return resultado