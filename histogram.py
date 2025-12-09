
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(200)

plt.hist(data, bins=20, edgecolor='black')
plt.title("Histogram of Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
