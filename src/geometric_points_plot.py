
import matplotlib.pyplot as plt


fig, graph = plt.subplots(figsize=(5, 2))

plt.scatter(2, 2, c="red")
plt.scatter(3, 3, c="blue")
plt.scatter(2, 4, c="green")

# Point names
names = ["A", "B", "C"]
points = [(2, 2), (3, 3), (2, 4)]

for name, point in zip(names, points):
    plt.annotate(name, point)

# Axis ranges
graph.set_yticks(range(1, 6))
graph.set_xticks(range(1, 6))

plt.title("Geometric Points")
plt.legend(["Point A", "Point B", "Point C"])
plt.show()
