import matplotlib.pyplot as plt
import numpy as np

# sucet = 0

# i = 1
# sucet = sucet + i
# i = 2
# sucet = sucet + i
# i = 3
# sucet = sucet + i
# i = 4
# sucet = sucet + i

# for i in range(1000000+1):
#     if i % 2 == 0:
#         sucet = sucet + i


# print(sucet)

def f(x):
    return x ** 2


def e(x):
    return 2 ** x


x = [i for i in range(-10, 10+1)]
y = [f(i) for i in range(-10, 10+1)]

y_e = [e(i) for i in range(-10, 10+1)]

print(x)
print(y)

plt.plot(x, y)
plt.plot(x, y_e)
plt.show()
