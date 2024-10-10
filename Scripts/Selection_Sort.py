
# Algoritmo para ordenar secuencas numericas
# buscando el minimo y posicionandolo en el primer lugar

lista_ordenada = []

def selection_sort(lista):

	global lista_ordenada

	if not type(lista) == list:
		return None

	for i in range(len(lista)):
		lista_ordenada.append(min(lista))
		lista.remove(min(lista))
		
	return lista_ordenada