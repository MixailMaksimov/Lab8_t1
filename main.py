import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.001)
y = 2 * np.sin(np.pi * 3 * x)
plt.plot(x, y)
plt.grid()
plt.show()