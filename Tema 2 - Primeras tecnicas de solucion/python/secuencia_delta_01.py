#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:24:04 2019

@author: gustavo
"""

import matplotlib.pyplot as plt
import numpy as np


def secuencia01(n, x):
    phi_nx = n/np.pi * (1 / (1 + (n**2 * x**2)))
    return phi_nx

n = 1

x = np.linspace(-10, 10, 200)

for i in [1,2,3]:
    plt.plot(x, secuencia01(i, x), label="n = " + str(i))
    
plt.title("Secuencia delta $\phi_{n}(x)$")    
plt.legend(loc=1)
plt.show()