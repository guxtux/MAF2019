import numpy as np
from scipy.special import j0, jn_zeros
import matplotlib.pyplot as plt

# Aceleracion debida a la gravedad s^-2
g = 9.81

# Longitud de la cadena, m
L = 1

# Amplitud máxima, m
A = 0.05

# Eje vertical (m)
z = np.linspace(0, L, 201)

# Eje vertical escalado
u = 2 * np.sqrt(z/g)

mode = 1

# jn_zeros calcula los primeros n ceros de Jo(x)
w = jn_zeros(0, mode)[mode-1] * np.sqrt(g/L) / 2


# Configura el espacio para la gráfica y los ejes
fig, ax = plt.subplots(figsize=(4,6))

ax.axis('off')
ax.set_xlim((-2*A, 2*A))
ax.set_ylim((0, L))
ax.set_title('Oscilación con m = {}'.format(mode))

line, = ax.plot([], [], 'k', dashes=[5, 2], lw=3)

interval = 10
i = 1
t = i * interval / 1000

x = A * j0(w*u) * np.cos(w*t)

plt.plot(z, x)
plt.show()