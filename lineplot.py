
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11, 1)
y = x

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Graph of y = x")
plt.grid(True)
plt.show()
