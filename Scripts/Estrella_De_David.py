
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (8, 5))

def crear_lineas(columna_1, columna_2):
	plt.plot(columna_1, columna_2, linestyle = "dotted", marker = "*")

crear_lineas([5, 3], [9, 3])
crear_lineas([5, 7], [9, 3])

crear_lineas([3, 7], [7, 7])
crear_lineas([3, 5], [7, 4])
crear_lineas([7, 5], [7, 4])

crear_lineas([5, 7], [4, 3])
crear_lineas([5, 3], [4, 3])

<<<<<<< HEAD
# Rangos para los ejes
=======
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
grafica.set_yticks(range(1, 11))
grafica.set_xticks(range(1, 11))

plt.title("Estrella De David")
plt.show()