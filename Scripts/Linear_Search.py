
<<<<<<< HEAD
# Algoritmo de busqueda numérica

def linear_search(lista, numero):
	return None if lista == [] else lista[0] if lista[0] == numero else linear_search(lista[1:], numero)
=======
# Algoritmo de busqueda numerica

def linear_search(lista, numero):

	if lista == []:
		return 

	else:

		if lista[0] == numero:
			return lista[0]
		return linear_search(lista[1:], numero)
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
