
import matplotlib.pyplot as plt

products = ['A', 'B', 'C', 'D']
sales = [40, 70, 30, 90]

plt.bar(products, sales)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales of Products")
plt.show()
