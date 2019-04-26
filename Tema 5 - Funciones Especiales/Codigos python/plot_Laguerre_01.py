#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:59:55 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_laguerre

x = np.linspace(0, 5, 200)

for i in range(6):
    plt.plot(x, eval_laguerre(i, x), color='k')

plt.title('Polinomios de Laguerre $L_{n}(x)$')
plt.text(1, 1.2, '$L_{0}$')
plt.text(3, -1.8, '$L_{1}$')
plt.text(3.2, -0.8, '$L_{2}$')
plt.text(4, 2.7, '$L_{3}$')
plt.text(4.5, 0.4, '$L_{4}$')
plt.text(4.2, -1.2, '$L_{5}$')
plt.axhline(y=0, lw=0.8, ls='dashed', color='k')
plt.xlim(0, 5)
#plt.ylim(-5, 5)
plt.show()
 
 