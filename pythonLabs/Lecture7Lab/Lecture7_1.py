import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**4 - 2*x - 2

# Define the x range for plotting
x = np.linspace(-3, 3, 400)
y = f(x)

# Create subplots for displaying the function graphs separately
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plot the function graphs
axs[0, 0].plot(x, y, label='x^4 - 2x - 2', color='blue', linestyle='-', linewidth=2)  # Blue solid line
axs[0, 1].plot(x, y - 0.5, label='Shifted Plot', color='green', linestyle='--', linewidth=2)  # Green dashed line
axs[1, 0].plot(x, y - 1, label='Another Shifted Plot', color='red', linestyle='-.', linewidth=2)  # Red dash-dot line
axs[1, 1].plot(x, y - 1.5, label='One More Shifted Plot', color='magenta', linestyle=':', linewidth=2)  # Magenta dotted line

# Set titles for each subplot
axs[0, 0].set_title('Graph 1: x^4 - 2x - 2')
axs[0, 1].set_title('Graph 2: Shifted Plot')
axs[1, 0].set_title('Graph 3: Another Shifted Plot')
axs[1, 1].set_title('Graph 4: One More Shifted Plot')

# Adding a legend to all subplots
for ax in axs.flat:
    ax.set(xlabel='x-axis', ylabel='y-axis')
    ax.legend()
    ax.grid()

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
