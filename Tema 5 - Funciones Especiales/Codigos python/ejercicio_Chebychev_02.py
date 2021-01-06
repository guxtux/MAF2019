
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x*800)/(x**2 + 54*x**4 + 3)

x = np.linspace(-1,1,200)

plt.plot(x, f(x))
plt.show()