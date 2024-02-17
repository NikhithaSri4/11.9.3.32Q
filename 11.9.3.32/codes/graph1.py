import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('values.dat')
x = data[:, 0]
y = data[:, 1]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

