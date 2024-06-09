
"""
Algoritmo de ordenamiento numerico: seleccionando 
el minimo o maximo y ordenandolo en base a estos
"""

def seleccion_directa(lista):

	try:
		lista_ordenada = []

		while len(lista) != 0:

			lista_ordenada.append(min(lista))
			lista.remove(min(lista))		
	
	except Exception as e:
		return f"Error: {e}"

	finally:
		return lista_ordenada

lista = [1, 4, 13, 7, 9, 0.5, 3, 10]
print(seleccion_directa(lista))