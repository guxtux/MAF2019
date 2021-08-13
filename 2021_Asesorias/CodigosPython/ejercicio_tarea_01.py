
import numpy as np
import matplotlib.pyplot as plt

def f(t, k, alfa):
    return np.exp(-k*np.abs(t)) * np.cos(alfa * t)

def solucion(alfa, k, omega):
    sol = (k /(2 * np.pi)) * ((1/((omega + alfa)**2) + k**2) + (1/((omega - alfa)**2) + k**2))
    return sol


t = np.linspace(-10, 10, 200)
t2 = np.linspace(-4, 4, 150)

alfa = 1
k = 0.2

plt.figure(1)
plt.plot(t, f(t, k, alfa))
plt.title("Gráfica de la función coseno amortiguado")
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
plt.axvline(x=0, ls='dashed', lw=0.7, color='k')
plt.xlim((-10,10))

plt.figure(2)
plt.plot(t2, solucion(alfa, k, t2))
plt.show()

