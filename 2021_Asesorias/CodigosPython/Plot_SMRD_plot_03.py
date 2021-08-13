#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:06:28 2018

@author: gustavo
"""

import numpy as np
import matplotlib.pylab as plt

def solucion(t):
    return 0.17241 * (-2 * np.cos(2 *t) + 5 * np.sin(2 * t))

def transitoria(t):
    return 0.06896 * (np.exp(-3 * t))* (5 * np.cos(5 * t) - 2 * np.sin(5 * t))

def periodica(t):
    return 0.17241 * (-2 * np.cos(2 * t) + 5 * np.sin(2 * t)) + ( 0.06896 * (np.exp(-3 * t))* (5 * np.cos(5 * t) - 2 * np.sin(5 * t)))


eje = np.linspace(0, 2.0)

plt.plot(eje, solucion(eje), color='b', label='Solución')
plt.plot(eje, transitoria(eje), color='r', label='Transitoria')
plt.plot(eje, periodica(eje), color='g', label='Periódica')
plt.legend(loc=1)

plt.xlim([0,2])
plt.axhline(y=0, color='k', lw=0.75, ls='dashed')
plt.show()