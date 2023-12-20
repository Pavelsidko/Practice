import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the system of nonlinear equations
def equations(vars):
    x, y = vars
    eq1 = y + np.exp(x) - 0.5
    eq2 = np.sin(y) - x - 1.5
    return [eq1, eq2]

# Solve the system of equations using fsolve from scipy
initial_guess = [0, 0]  # Provide initial guess for the solution
solution = fsolve(equations, initial_guess)

# Define the range for x
x = np.linspace(-2, 2, 400)
# Calculate the corresponding y values based on the first equation
y1 = - np.exp(x) + 0.5
# Calculate the corresponding y values based on the second equation
y2 = np.arcsin(x - 1.5)

# Plot the functions
plt.plot(x, y1, label='y + e^x = 0.5', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y2, label='sin(y) - x = 1.5', color='red', linestyle='--', linewidth=2)

# Plot the solution point
plt.scatter(solution[0], solution[1], color='green', label='Solution')  # Mark the solution point

# Title and labels
plt.title('Graphical Solution to System of Nonlinear Equations')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Legend
plt.legend()

# Annotations
plt.text(solution[0], solution[1], f'Solution: ({solution[0]:.2f}, {solution[1]:.2f})', fontsize=12)

# Grid and scaling
plt.grid(True)

# Display the plot
plt.show()
