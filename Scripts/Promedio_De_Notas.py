
# Promedio de 4 notas
def promedio(notas):
	try:
		if len(notas) != 4 or len(notas) < 4:
			return "Ingrese una lista de 4 notas"
		return round(sum(notas) / 4)
	
	except Exception as e:
		print(f"Error inesperado: {e}")