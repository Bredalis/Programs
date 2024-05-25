
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (5, 3))

plt.plot([1, 0], [5, 3])
plt.plot([0, 3], [3, 1])
plt.plot([1, 3], [5, 1])

plt.text(x = 1, y = 3, s = "Sy")

grafica.set_yticks(range(1, 6))
grafica.set_xticks(range(1, 6))

plt.title("Rectangulo")
plt.show()