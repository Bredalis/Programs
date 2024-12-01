
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (5, 3))

plt.plot([2, 2], [5, 2], marker = "o")
plt.plot([2, 7], [5, 2], marker = "o")
plt.plot([2, 7], [2, 2], marker = "o")

grafica.set_yticks(range(1, 8))
grafica.set_xticks(range(1, 8))

plt.title("Triángulo")
plt.show()