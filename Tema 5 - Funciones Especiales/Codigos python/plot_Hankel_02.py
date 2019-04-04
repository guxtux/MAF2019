#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:06:49 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

x = np.linspace(0, 10, 100)

for v in range(0, 4):
    plt.plot(x, sp.jv(v, x))
    plt.plot(x, -1*sp.yv(v, x), '--')


plt.axhline(y=0, lw=0.9)
plt.xlim([0, 10])
plt.ylim([-1, 2])
plt.title(r'Funciones de Hankel $H_{\nu}^{(2)}(x)$')
plt.show()