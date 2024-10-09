
# Algoritmo numerico

def insertion_sort(lista):

	lista_ordenada = []

	for i in range(len(lista)):

		lista_ordenada.insert(0, max(lista))
		lista.remove(max(lista))		

	return lista_ordenada