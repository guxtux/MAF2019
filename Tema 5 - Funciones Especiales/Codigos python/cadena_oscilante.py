# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
from scipy.special import j0, jn_zeros
import matplotlib.pyplot as plt
from matplotlib import animation
#from IPython.display import HTML

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

mode = 2
# jn_zeros calcula los primeros n ceros de Jo(x)
w = jn_zeros(0, mode)[mode-1] * np.sqrt(g/L) / 2


# Configura el espacio para la gráfica y los ejes
fig, ax = plt.subplots(figsize=(4,6))

ax.axis('off')
ax.set_xlim((-2*A, 2*A))
ax.set_ylim((0, L))
ax.set_title('m = {}'.format(mode))

line, = ax.plot([], [], 'k', dashes=[5,2], lw=3)


# Da inicio a la funcion para la animacion
def init():
    line.set_data([], [])
    return (line,)


# Retraso entre los frames (ms)
interval = 10
# Total de frames en la animacion para tener un periodo de oscilacion completo
nframes = int(2 * np.pi / w * 1000 / interval)

# Llamada secuencial para la funcion de animacion
def animate(i):
    t = i * interval / 1000
    x = A * j0(w*u) * np.cos(w*t)
    line.set_data(x, z)
    return (line,)


# Configuracion de la animacion
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nframes, interval=interval, blit=True)


# Se guarda la animacion en un archivo gif
anim.save('chain_{}.gif'.format(mode), writer='imagemagick', fps=1000/interval)