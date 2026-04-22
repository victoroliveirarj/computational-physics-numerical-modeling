import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.title("Scientific Visualization Example")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
