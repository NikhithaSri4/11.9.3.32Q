import matplotlib.pyplot as plt
import numpy as np

# Define the quadratic function
def quadratic_function(x):
    return x**2 - 16*x + 25

# Generate x values
x_values = np.linspace(-5, 21, 100)

# Calculate corresponding y values
y_values = quadratic_function(x_values)

# Plot the graph
plt.plot(x_values, y_values, label='$x^2 - 16x + 25$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Graph of $x^2 - 16x + 25$')
plt.grid(False)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()
