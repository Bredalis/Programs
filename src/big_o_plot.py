
# Algorithm time complexity graph (Big O)

import matplotlib.pyplot as plt
import numpy as np


def plot_graph(x_values, y_values, color, label):
    """Plot a curve with a label."""
    plt.plot(x_values, y_values, color=color, label=label)


# Big O notation input values
n_values = np.linspace(1, 100, 400)

# Plot different complexities
plot_graph(n_values, n_values ** 2, "red", "O(n^2)")
plot_graph(n_values, n_values, "blue", "O(n)")
plot_graph(n_values, np.log(n_values), "yellow", "O(log n)")
plot_graph(n_values, np.ones_like(n_values), "green", "O(1)")

# Graph properties
plt.title("Big O Notation")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.legend()

# Axis scaling
plt.yscale("log")
plt.xscale("linear")
plt.grid(True)

plt.show()
