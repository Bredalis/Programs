
# Algoritmo para ordenar secuencas numericas
# buscando el minimo y posicionandolo en el primer lugar

lista_ordenada = []

def selection_sort(lista):

	global lista_ordenada

	for i in range(len(lista)):
		lista_ordenada.append(min(lista))
		lista.remove(min(lista))
		
	print(lista_ordenada)
	
lista = [5, 3, 1, 4, 2]
selection_sort(lista)