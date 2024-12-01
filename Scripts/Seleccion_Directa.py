
"""
Algoritmo de ordenamiento: seleccionar 
el mínimo o máximo y ordenarlo en base a este
"""

# A partir del mínimo
def seleccion_directa(lista):
	try:
		lista_ordenada = []

		while len(lista) != 0:
			lista_ordenada.append(min(lista))
			lista.remove(min(lista))		
	
	except Exception as e:
		return f"Error inesperado: {e}"

	finally:
		return lista_ordenada