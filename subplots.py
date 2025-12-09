
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x))
plt.title("Line Plot")

plt.subplot(2, 2, 2)
plt.scatter(x, np.cos(x))
plt.title("Scatter Plot")

plt.subplot(2, 2, 3)
plt.bar(['A', 'B', 'C'], [5, 7, 3])
plt.title("Bar Plot")

plt.subplot(2, 2, 4)
plt.hist(np.random.randn(100))
plt.title("Histogram")

plt.tight_layout()
plt.show()
