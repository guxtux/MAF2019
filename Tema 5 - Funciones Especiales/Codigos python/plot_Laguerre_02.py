#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:59:55 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_genlaguerre

x = np.linspace(0, 5, 200)

plt.plot(x, eval_genlaguerre(0, 0, x), color='k', ls='--', dashes=[3, 1])
plt.plot(x, eval_genlaguerre(1, 0, x), color='k', ls='--', dashes=[2, 1, 3, 2])
plt.plot(x, eval_genlaguerre(2, 0, x), color='k', ls='--', dashes=[5, 2])
plt.plot(x, eval_genlaguerre(2, 1, x), color='k', ls='--', dashes=[1, 3, 2, 1])
plt.plot(x, eval_genlaguerre(3, 0, x), color='k', ls='--', dashes=[2, 1, 1, 2])
plt.plot(x, eval_genlaguerre(3, 1, x), color='k')
#plt.plot(x, eval_genlaguerre(3, 2, x), color='k')

plt.title('Polinomios asociados de Laguerre $L_{n}^{k}(x)$')
plt.text(2, 1.3, '$L_{0}^{0}$')
plt.text(4, -2.6, '$L_{1}^{0}$')
plt.text(3.8, 0.2, '$L_{2}^{0}$')
plt.text(4.5, -0.8, '$L_{2}^{1}$')
plt.text(3.6, 2.3, '$L_{3}^{0}$')
plt.text(0.3, 3.2, '$L_{3}^{1}$')
plt.axhline(y=0, lw=0.8, ls='dashed', color='k')
plt.xlim(0, 5)
plt.show()
 
 