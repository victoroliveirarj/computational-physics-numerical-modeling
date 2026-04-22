import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 10, 300)
x = np.cos(t)

plt.figure(figsize=(8, 5))
plt.plot(t, x)
plt.title("Simple Physical Simulation Example")
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.grid(True)
plt.show()
