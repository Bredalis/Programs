
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(7, 4))


def create_line(x_values, y_values):
    """Draws a line segment."""
    ax.plot(x_values, y_values)


# Head
create_line([4, 6], [6, 6])

# Right ear
create_line([4, 3.5], [6, 7])
create_line([3, 3.5], [6, 7])

# Left ear
create_line([6, 6.5], [6, 7])
create_line([6.5, 7], [7, 6])

# Chin
create_line([3, 5], [6, 2])
create_line([7, 5], [6, 2])

# Eyes and nose
ax.scatter([4.5, 5.5], [5, 5], s=100)
ax.scatter([5], [4], s=100)

# Right whiskers
create_line([5, 4.3], [4, 4.3])
create_line([5, 4.3], [4, 4])
create_line([5, 4.3], [4, 3.7])

# Left whiskers
create_line([5, 5.7], [4, 4.3])
create_line([5, 5.7], [4, 4])
create_line([5, 5.7], [4, 3.7])

# Axis ranges
ax.set_xticks(range(1, 9))
ax.set_yticks(range(1, 9))

plt.title("Cat Face")
plt.show()
