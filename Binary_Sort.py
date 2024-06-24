
# Es un algoritmo eficiente para encontrar 
# un elemento en una lista ordenada

def binary_search(lista, numero):

	# Posiciones de la lista
	
	lista.sort()
	centro = len(lista) // 2
	izquierda = lista[:centro]
	derecha = lista[centro:]

	if lista[centro] == numero:
		return f"{numero} esta en el centro"

	if numero in izquierda:
		return f"{numero} esta en la izquierda"

	if numero in derecha:
		return f"{numero} esta en la derecha"

	return "El numero no esta"

lista = [11, 33, 5, 25, 8, 64, 90]
print(binary_search(lista, 5))