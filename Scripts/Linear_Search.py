
# Algoritmo de busqueda numerica

def linear_search(lista, numero):

	if lista == []:
		return 

	else:

		if lista[0] == numero:
			return lista[0]
		return linear_search(lista[1:], numero)