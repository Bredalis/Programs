
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (7, 4))

# Cabeza

plt.plot([4, 6], [6, 6])

# Oreja derecha

plt.plot([4, 3.5], [6, 7])
plt.plot([3, 3.5], [6, 7])

# Oreja izquierda

plt.plot([6, 6.5], [6, 7])
plt.plot([6.5, 7], [7, 6])

# Barbilla

plt.plot([3, 5], [6, 2])
plt.plot([7, 5], [6, 2])

# Ojos y nariz

plt.scatter([4.5, 5.5], [5, 5], s = 100)
plt.scatter([5], [4], s = 100)

# Bigotes derechos

plt.plot([5, 4.3], [4, 4.3])
plt.plot([5, 4.3], [4, 4])
plt.plot([5, 4.3], [4, 3.7])

# Bigotes izquierdos

plt.plot([5, 5.7], [4, 4.3])
plt.plot([5, 5.7], [4, 4])
plt.plot([5, 5.7], [4, 3.7])

grafica.set_yticks(range(1, 9))
grafica.set_xticks(range(1, 9))

plt.title("Cara De Gato")
plt.show()