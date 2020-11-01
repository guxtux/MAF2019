#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:55:12 2019

@author: gustavo
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def secuencia03(n, x):
    phi_nx = 1/(n *np.pi) * (np.sin(n*x)**2/x**2)
    return phi_nx

x = np.linspace(-5, 5, 200)

for i in [1,2,3]:
    plt.plot(x, secuencia03(i, x), label="n = " + str(i))
    
plt.title(r"Secuencia delta $\phi_{n}(x)$", fontsize=16)
plt.text(-5,0.5,r"$\phi_{n} = \dfrac{1}{n \, \pi} \, \dfrac{\sin^{2} n x}{x^{2}}$", fontsize=16)
plt.legend(loc=1)
plt.show()