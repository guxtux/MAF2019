
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x+1)

def f_i(x):
    return (2*np.exp(0) - 4 * np.exp(3./2) + 2*np.exp(2)) * x**2 + (-3*np.exp(0) - 4 * np.exp(3./2) + 2*np.exp(2)) * x + np.exp(0)

x = np.linspace(0, 1.1, 200)

plt.plot(x,f(x), ls='dashed', lw=0.7)
plt.plot(x, f_i(x))
plt.plot(0, f(0), 'or', 0.5, f(0.5), 'or', 1, f(1), 'or')
plt.xlim((0,1.1))
plt.title('Gráfica de f(x) y los puntos a interpolar')
plt.show()