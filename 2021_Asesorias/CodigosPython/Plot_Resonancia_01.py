#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:55:22 2018

@author: gustavo
"""

import numpy as np
import matplotlib.pylab as plt
import matplotlib.ticker as tck

def solucion(t):
    return 0.125*(np.sin(2 * t) - 2 * t * np.cos(2 * t))

def envolventes(x):
    return 0.125*np.sqrt((4 * x**2) + 1)
    
eje = np.linspace(0,4*np.pi,500)

f, ax=plt.subplots(1)

ax.plot(eje, solucion(eje), color='blue')
ax.plot(eje, envolventes(eje), color='red', lw=0.75)
ax.plot(eje, -envolventes(eje), color='red', lw=0.75)
ax.set_xlim([0,4*np.pi])
ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
ax.text(2, 1.5, '$+C(t)$')
ax.text(2, -1.5, '$-C(t)$')
plt.axhline(y=0, color='k', lw=0.75, ls='dashed')
plt.title('Solución del desplazamiento con las curvas envolventes')
#ax.xaxis.set_major_locator(tck.matplotlib.ticker.MultipleLocator(base=1.0))
plt.show()