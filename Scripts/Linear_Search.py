
# Algoritmo de busqueda numérica

def linear_search(lista, numero):
	return None if lista == [] else lista[0] if lista[0] == numero else linear_search(lista[1:], numero)