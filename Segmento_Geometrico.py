
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (7, 3))

plt.plot([0, 5], [3, 3])
plt.plot([2, 2], [4, 0])
plt.plot([4, 4], [4, 0])

plt.annotate("A", (0, 3))
plt.annotate("D", (5, 3))
plt.annotate("B", (2, 4))
plt.annotate("C", (4, 4))

grafica.set_yticks(range(1, 6))
grafica.set_xticks(range(1, 6))

plt.title("Segmento Geometrico")
plt.legend(["Recta AD", "Segmento BC"])
plt.show()