#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:24:04 2019

@author: gustavo
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def secuencia01(n, x):
    phi_nx = n/np.pi * (1 / (1 + (n**2 * x**2)))
    return phi_nx

n = 1

x = np.linspace(-10, 10, 200)


for i in [1,2,3]:
    plt.plot(x, secuencia01(i, x), label="n = " + str(i))
    
plt.title(r"Secuencia delta $\phi_{n}(x)$", fontsize=16)
plt.text(-9.75,0.5,r"$\phi_{n} = \dfrac{n}{\pi} \, \dfrac{1}{(1 + x^{2}) \, n^{2}}$", fontsize=16)
plt.legend(loc=1)
plt.show()