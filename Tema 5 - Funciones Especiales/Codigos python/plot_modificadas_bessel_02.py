#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:06:49 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

x = np.linspace(0, 10)

for v in range(0, 2):
    plt.plot(x, sp.kv(v, x), label='$K_{' + str(v)+ '}$')

plt.legend(loc='best')
plt.axhline(y=0, lw=0.9)
#plt.xlim([4, 10])
#plt.ylim([-4, 1])
plt.title(r'Funciones modificadas de Bessel $K_{\nu}(x)$')
plt.show()