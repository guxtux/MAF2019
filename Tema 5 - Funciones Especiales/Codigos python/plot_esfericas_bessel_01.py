#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:06:49 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

x = np.linspace(0, 14)

for v in range(0, 4):
    plt.plot(x, sp.spherical_jn(v, x, 0))
        


plt.axhline(y=0, lw=0.9)
plt.xlim([0, 14])
#plt.ylim([-4, 2])
plt.title(r'Funciones esféricas de Bessel $j_{n}(x)$')
plt.show()