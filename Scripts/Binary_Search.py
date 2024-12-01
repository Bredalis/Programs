
# Algoritmo para encontrar 
# un elemento en una lista ordenada

def binary_search(lista, numero):

	# Posiciones de la lista
	lista.sort()
	centro = len(lista) // 2
	izquierda = lista[:centro]
	derecha = lista[centro:]

	if len(lista) == 0:
		return "Lista vacía"

	if lista[centro] == numero:
		return f"{numero} esta en el centro"

	if numero in izquierda:
		return f"{numero} esta en la izquierda"

	if numero in derecha:
		return f"{numero} esta en la derecha"

	return "El número no esta"