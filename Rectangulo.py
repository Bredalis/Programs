
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (5, 4))

plt.plot([4, 8], [7, 7], marker = "o")
plt.plot([4, 8], [2, 2], marker = "o")

plt.plot([4, 4], [7, 2], marker = "o")
plt.plot([8, 8], [2, 7], marker = "o")

grafica.set_yticks(range(1, 9))
grafica.set_xticks(range(1, 9))

plt.title("Rectangulo")
plt.show()