
# Gráfica del tiempo algorítmico

import matplotlib.pyplot as plt
import numpy as np

# Valor de la Notación Big O
n = np.linspace(1, 100, 400)

def grafica(x, y, color, algoritmo):
	plt.plot(x, y, color = color, label = algoritmo)

grafica(n, n ** 2, "red", "O(n^2)")
grafica(n, n, "blue", "O(n)")
grafica(n, np.log(n), "yellow", "O(log n)")
grafica(n, np.ones_like(n), "green", "O(1)")

# Propiedadse de la gráfica
plt.title("Notación Big O")
plt.xlabel("Tamaño")
plt.ylabel("Tiempo")
plt.legend()

# Cambiar la escala de los ejes
plt.yscale("log")
plt.xscale("linear")
plt.grid(True)
plt.show()