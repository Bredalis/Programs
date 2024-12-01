
# Calcula la relación binaria de dos conjuntos
# Pasos para resolver la operación:
# -> Sacar producto cartesiano
# -> Resolución del enunciado
# -> Mostrar Conjunto Solución

from itertools import product

def producto_cartesiano(a = None, b = None):
	try:
		return list(product(a, b))
	except Exception as e:
		print(f"Error inesperado: {e}")

def relacion_binaria(pc, enunciado):
	try:
		return list(filter(enunciado, pc))
	except Exception as e:
		print(f"Error inesperado: {e}")