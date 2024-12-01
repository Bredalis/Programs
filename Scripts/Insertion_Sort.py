
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