
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (5, 2))
<<<<<<< HEAD
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
=======

# Puntos

punto_a = [2], [2]
punto_b = [3], [3]
punto_c = [2], [4]

plt.scatter(punto_a[0], punto_a[1], c = "red")
plt.scatter(punto_b[0], punto_b[1], c = "blue")
plt.scatter(punto_c[0], punto_c[1], c = "green")

# Nombres de los puntos

nombres = ["A", "B", "C"]
puntos = [punto_a, punto_b, punto_c]

for n, p in zip(nombres, puntos):
	plt.annotate(n, (p[0][0], p[1][0]))

grafica.set_yticks(range(1, 6))
grafica.set_xticks(range(1, 6))

plt.title("Puntos Geometricos")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
plt.legend(["Punto A", "Punto B", "Punto C"])
plt.show()