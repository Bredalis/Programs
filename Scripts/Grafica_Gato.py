
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (7, 4))

def crear_lineas(columna_1, columna_2):
	plt.plot(columna_1, columna_2)

# Cabeza
crear_lineas([4, 6], [6, 6])

# Oreja derecha
crear_lineas([4, 3.5], [6, 7])
crear_lineas([3, 3.5], [6, 7])

# Oreja izquierda
crear_lineas([6, 6.5], [6, 7])
crear_lineas([6.5, 7], [7, 6])

# Barbilla
crear_lineas([3, 5], [6, 2])
crear_lineas([7, 5], [6, 2])

# Ojos y nariz
plt.scatter([4.5, 5.5], [5, 5], s = 100)
plt.scatter([5], [4], s = 100)

# Bigotes derechos
crear_lineas([5, 4.3], [4, 4.3])
crear_lineas([5, 4.3], [4, 4])
crear_lineas([5, 4.3], [4, 3.7])

# Bigotes izquierdos
crear_lineas([5, 5.7], [4, 4.3])
crear_lineas([5, 5.7], [4, 4])
crear_lineas([5, 5.7], [4, 3.7])

# Rangos de los ejes
grafica.set_yticks(range(1, 9))
grafica.set_xticks(range(1, 9))

plt.title("Cara De Gato")
plt.show()