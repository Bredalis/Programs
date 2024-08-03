
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (6, 4))

def crear_lineas(columna_1, columna_2, texto):
	plt.plot(columna_1, columna_2, label = texto)

crear_lineas([2, 4], [2, 4], "Recta CD")
crear_lineas([5, 3], [2, 2], "Recta MN")
crear_lineas([1, 2], [3, 5], "Recta AB")

# Nombrar rectas

def crear_textos(letra, posicion):
	plt.annotate(letra, posicion)

crear_textos("C", (2, 2))
crear_textos("D", (4, 4))
crear_textos("M", (3, 2))
crear_textos("N", (5, 2))
crear_textos("A", (1, 3))
crear_textos("B", (2, 5))

grafica.set_yticks(range(1, 6))
grafica.set_xticks(range(1, 6))

plt.title("Rectas Geometricas")
plt.legend()
plt.show()