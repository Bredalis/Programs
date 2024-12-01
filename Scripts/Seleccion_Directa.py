
"""
<<<<<<< HEAD
Algoritmo de ordenamiento: seleccionar 
el mínimo o máximo y ordenarlo en base a este
"""

# A partir del mínimo
def seleccion_directa(lista):
=======
Algoritmo de ordenamiento numerico: seleccionando 
el minimo o maximo y ordenandolo en base a estos
"""

def seleccion_directa(lista):

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	try:
		lista_ordenada = []

		while len(lista) != 0:
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
			lista_ordenada.append(min(lista))
			lista.remove(min(lista))		
	
	except Exception as e:
<<<<<<< HEAD
		return f"Error inesperado: {e}"

	finally:
		return lista_ordenada
=======
		return f"Error: {e}"

	finally:
		return lista_ordenada

lista = [1, 4, 13, 7, 9, 0.5, 3, 10]
print(seleccion_directa(lista))
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
