
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(8, 5))


def create_line(x_values, y_values):
    """Draws a dotted line with star markers."""
    ax.plot(x_values, y_values, linestyle="dotted", marker="*")


create_line([5, 3], [9, 3])
create_line([5, 7], [9, 3])

create_line([3, 7], [7, 7])
create_line([3, 5], [7, 4])
create_line([7, 5], [7, 4])

create_line([5, 7], [4, 3])
create_line([5, 3], [4, 3])

# Axis ranges
ax.set_xticks(range(1, 11))
ax.set_yticks(range(1, 11))

plt.title("Star of David")
plt.show()
