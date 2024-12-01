
print("\nTabla de Multiplicación")

def tabla_muplicacion(numero: int):
	print(f"\nTabla {numero}")
	return [f"{numero} X {i} = {i * numero}" for i in range(0, 11)]