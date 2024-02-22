import numpy as np
import matplotlib.pyplot as plt

# Load data from values.dat
data = np.loadtxt('values.dat')
x = data[:, 0]
y = data[:, 1]

# Plot for values.dat
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) ')
plt.grid(True)
plt.savefig('f1.png', dpi = 300, bbox_inches = 'tight')

# Load data from values1.dat
data = np.loadtxt('values1.dat')
n = data[:, 0].astype(int)
xn = data[:, 1]

# Plot for values1.dat
plt.subplot(2, 2, 3)
plt.stem(n, xn)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Plot of AP series')
plt.grid(True)
plt.savefig('ap.png', dpi = 300, bbox_inches = 'tight')

# Load data from values2.dat
data = np.loadtxt('values2.dat')
n = data[:, 0].astype(int)
xn = data[:, 1]

# Plot for values2.dat
plt.subplot(2, 2, 4)
plt.stem(n, xn)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Plot of GP series ')
plt.grid(True)
plt.savefig('gp.png', dpi = 300, bbox_inches = 'tight')

plt.tight_layout()
plt.show()

