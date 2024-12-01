
<<<<<<< HEAD
print("\nTabla de Multiplicación")

def tabla_muplicacion(numero: int):
	print(f"\nTabla {numero}")
	return [f"{numero} X {i} = {i * numero}" for i in range(0, 11)]
=======
print("\nTabla de Multiplicacion")

def tablas_muplicacion(numero: int):

	resultado = []
	print(f"\n{"Tabla"} {numero}")

	for i in range(0, 11):
		resultado.append(f"{i} X {numero} = {i * numero}")

	return resultado
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
