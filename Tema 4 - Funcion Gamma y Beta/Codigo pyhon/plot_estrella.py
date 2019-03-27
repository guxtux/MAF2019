#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:05:57 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 2.
c = 3.
t = np.linspace(-1, 1, 500)

def y1(x):
    return (1 - x**(b/c))**(c/b)

def y2(x):
    return -(1 - x**(b/c))**(c/b)

plt.plot(t, y1(t), color='k')
plt.plot(t, y2(t), color='k')
plt.plot(-y1(t), t, color='k')
plt.plot(y2(t), -t, color='k')

plt.axhline(y=0, lw=0.8, color='k')
plt.axvline(x=0, lw=0.8, color='k')
# Turn off tick labels
plt.gca().axes.get_yaxis().set_visible(False)
plt.gca().axes.get_xaxis().set_visible(False)

plt.title('Curva $x^{b/c} + y^{b/c} = a^{b/c}$ donde $b < c$')
plt.show()