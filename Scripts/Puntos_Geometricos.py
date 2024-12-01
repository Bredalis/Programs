
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (5, 2))
plt.scatter(2, 2, c = "red")
plt.scatter(3, 3, c = "blue")
plt.scatter(2, 4, c = "green")

# Nombres de los puntos
nombres = ["A", "B", "C"]
puntos = [(2, 2), (3, 3), (2, 4)]

for n, p in zip(nombres, puntos):
	plt.annotate(n, p)

# Rangos de los ejes
grafica.set_yticks(range(1, 6))
grafica.set_xticks(range(1, 6))

plt.title("Puntos Geométricos")
plt.legend(["Punto A", "Punto B", "Punto C"])
plt.show()