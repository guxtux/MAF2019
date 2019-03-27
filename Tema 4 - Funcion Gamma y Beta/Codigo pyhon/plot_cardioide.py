#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:34:14 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

a = 1
t = np.linspace(0, np.pi, num=1000)

def curva(t):
    x = a * (t + np.sin(t))
    y = a * (1 - np.cos(t))
    return x, y

plt.plot(curva(t)[0], curva(t)[1])
plt.plot(np.pi, 2,'o', color='k')
plt.plot(curva(np.pi*0.5)[0], curva(np.pi*0.5)[1], 'o', color='k')
plt.text(2.6, 2, '$(a \, \pi, 2 \, a)$')
plt.text(2.1, 1, '$(x_{1}, y_{1})$')
plt.axhline(y=0, lw=0.8, color='k')
plt.axvline(x=0, lw=0.8, color='k')
plt.text(-0.1, -0.1, '$O$')
# Turn off tick labels
plt.gca().axes.get_yaxis().set_visible(False)
plt.gca().axes.get_xaxis().set_visible(False)
plt.xlim(0, 3.4)
plt.ylim(0, 2.1)
plt.title('Parte de una cicloide')
plt.show()