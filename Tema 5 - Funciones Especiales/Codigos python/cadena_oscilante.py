# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
from scipy.special import j0, jn_zeros
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML

# Acceleration due to gravity, m.s-2
g = 9.81
# Chain length, m
L = 1
# Maximum amplitude, m
A = 0.05
# Vertical axis (m)
z = np.linspace(0, L, 201)
# Scaled vertical axis
u = 2 * np.sqrt(z/g)

mode = 4
# jn_zeros calculates the first n zeros of the zero-th order Bessel function of the first kind
w = jn_zeros(0, mode)[mode-1] * np.sqrt(g/L) / 2


# Set up the Figure and Axes
fig, ax = plt.subplots(figsize=(4,6))

ax.axis('off')
ax.set_xlim((-2*A, 2*A))
ax.set_ylim((0, L))
ax.set_title('m = {}'.format(mode))

line, = ax.plot([], [], 'k', dashes=[5,2], lw=3)


# Initialization function for the animation
def init():
    line.set_data([], [])
    return (line,)


# Delay between frames (ms)
interval = 10
# Total number of frames in the animation so that the animation is for one period of oscillation
nframes = int(2 * np.pi / w * 1000 / interval)

# The animation function, to be called sequentially
def animate(i):
    t = i * interval / 1000
    x = A * j0(w*u) * np.cos(w*t)
    line.set_data(x, z)
    return (line,)


# Set up the animation
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nframes, interval=interval, blit=True)


# To save the animation as a gif, run this cell.
anim.save('chain_{}.gif'.format(mode), writer='imagemagick', fps=1000/interval)