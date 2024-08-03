
# Algoritmo de busqueda numerica

def linear_search(lista, numero):

	if lista == []:
		return 

	else:

		if lista[0] == numero:
			return lista[0]
		return linear_search(lista[1:], numero)

lista = [1, 2, 3, 4]
print(linear_search(lista, 2))