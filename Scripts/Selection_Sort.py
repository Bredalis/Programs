
# Algoritmo para ordenar secuencas numericas
# buscando el minimo y posicionandolo en el primer lugar

<<<<<<< HEAD
def selection_sort(lista):
    if not isinstance(lista, list):
        return None

    lista_ordenada = []
    lista_copia = lista.copy()

    for _ in range(len(lista_copia)):
        minimo = min(lista_copia)
        lista_ordenada.append(minimo)
        lista_copia.remove(minimo)

    return lista_ordenada
=======
lista_ordenada = []

def selection_sort(lista):

	global lista_ordenada

	if not type(lista) == list:
		return None

	for i in range(len(lista)):
		lista_ordenada.append(min(lista))
		lista.remove(min(lista))
		
	return lista_ordenada
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
