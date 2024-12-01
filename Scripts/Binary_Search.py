
<<<<<<< HEAD
# Algoritmo para encontrar 
=======
# Es un algoritmo eficiente para encontrar 
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
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