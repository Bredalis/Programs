
import matplotlib.pyplot as plt

fig, grafica = plt.subplots(figsize = (8, 5))

plt.plot([5, 3], [9, 3], linestyle = "dotted", marker = "*")
plt.plot([5, 7], [9, 3], linestyle = "dotted", marker = "*")

plt.plot([3, 7], [7, 7], linestyle = "dotted", marker = "*")
plt.plot([3, 5], [7, 4], linestyle = "dotted", marker = "*")
plt.plot([7, 5], [7, 4], linestyle = "dotted", marker = "*")

plt.plot([5, 7], [4, 3], linestyle = "dotted", marker = "*")
plt.plot([5, 3], [4, 3], linestyle = "dotted", marker = "*")

grafica.set_yticks(range(1, 11))
grafica.set_xticks(range(1, 11))

plt.title("Estrella De David")
plt.show()