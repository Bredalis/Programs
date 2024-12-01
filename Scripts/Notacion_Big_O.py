
<<<<<<< HEAD
# Gráfica del tiempo algorítmico
=======
# Grafica del tiempo algoritmico
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

import matplotlib.pyplot as plt
import numpy as np

<<<<<<< HEAD
# Valor de la Notación Big O
=======
# Valor de la Notacion Big O

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
n = np.linspace(1, 100, 400)

def grafica(x, y, color, algoritmo):
	plt.plot(x, y, color = color, label = algoritmo)

grafica(n, n ** 2, "red", "O(n^2)")
grafica(n, n, "blue", "O(n)")
grafica(n, np.log(n), "yellow", "O(log n)")
grafica(n, np.ones_like(n), "green", "O(1)")

<<<<<<< HEAD
# Propiedadse de la gráfica
plt.title("Notación Big O")
=======
plt.title("Notacion Big O")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
plt.xlabel("Tamaño")
plt.ylabel("Tiempo")
plt.legend()

# Cambiar la escala de los ejes
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
plt.yscale("log")
plt.xscale("linear")
plt.grid(True)
plt.show()