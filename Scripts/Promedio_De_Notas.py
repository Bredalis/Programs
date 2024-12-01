
# Promedio de 4 notas
<<<<<<< HEAD
def promedio(notas):
	try:
		if len(notas) != 4 or len(notas) < 4:
			return "Ingrese una lista de 4 notas"
		return round(sum(notas) / 4)
	
	except Exception as e:
		print(f"Error inesperado: {e}")
=======

def promedio(notas):
	
	if len(notas) != 4 or len(notas) < 4:
		return "Tiene que ingresar 4 notas" 

	promedio = sum(notas) / 4 
	return promedio

notas = [56, 70, 88, 88]
print(promedio(notas))
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
