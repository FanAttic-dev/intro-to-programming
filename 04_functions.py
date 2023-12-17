import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-7, 7, 0.1)
print(x)


def square(x):
    return np.power(x, 2)


y = square(x)
plt.plot(x, y)


def exponentiate(x):
    return np.power(2, x)


y = exponentiate(x)
plt.plot(x, y)
plt.axvline(x=0, c="black", label="x=0")
plt.axhline(y=0, c="black", label="y=0")
plt.axis([-5, 5, -2, 2])

plt.show()
