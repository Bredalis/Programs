
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (5, 3))

plt.plot([2, 2], [5, 2], marker = "o")
plt.plot([2, 7], [5, 2], marker = "o")
plt.plot([2, 7], [2, 2], marker = "o")

grafica.set_yticks(range(1, 8))
grafica.set_xticks(range(1, 8))

<<<<<<< HEAD
plt.title("Triángulo")
=======
plt.title("Triangulo")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
plt.show()