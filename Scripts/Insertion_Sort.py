
<<<<<<< HEAD
# Algoritmo numérico

def insertion_sort(lista):
	try:
		lista_ordenada = []

		for i in range(len(lista)):
			lista_ordenada.insert(0, max(lista))
			lista.remove(max(lista))
		return lista_ordenada

	except Exception as e:
		return f"Error inesperado: {e}"
=======
# Algoritmo numerico

def insertion_sort(lista):

	lista_ordenada = []

	for i in range(len(lista)):

		lista_ordenada.insert(0, max(lista))
		lista.remove(max(lista))		

	return lista_ordenada
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
