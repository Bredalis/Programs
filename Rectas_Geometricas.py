
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (6, 4))

plt.plot([2, 4], [2, 4], label = "Recta CD")
plt.plot([5, 3], [2, 2], label = "Recta MN")
plt.plot([1, 2], [3, 5], label = "Recta AB")

# Nombrar rectas

plt.annotate("C", (2, 2))
plt.annotate("D", (4, 4))
plt.annotate("M", (3, 2))
plt.annotate("N", (5, 2))
plt.annotate("A", (1, 3))
plt.annotate("B", (2, 5))

grafica.set_yticks(range(1, 6))
grafica.set_xticks(range(1, 6))

plt.title("Rectas Geometricas")
plt.legend()
plt.show()