#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:45:00 2019

@author: gustavo
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def secuencia02(n, x):
    phi_nx = n/np.sqrt(np.pi) * np.exp(-n**2 * x**2)
    return phi_nx

x = np.linspace(-5, 5, 200)

for i in [1,2,3]:
    plt.plot(x, secuencia02(i, x), label="n = " + str(i))
    
plt.title(r"Secuencia delta $\phi_{n}(x)$", fontsize=16)
plt.text(-4.5,0.8,r"$\phi_{n} = \dfrac{n}{\sqrt{\pi}} \, e^{-n^{2} \, x^{2}}$", fontsize=16)
plt.legend(loc=1)
plt.show()