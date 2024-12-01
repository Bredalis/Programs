
# Algoritmo para ordenar secuencas numericas
# buscando el minimo y posicionandolo en el primer lugar

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