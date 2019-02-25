#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 13:42:21 2019

@author: gustavo
"""

import matplotlib.pyplot as plt
import numpy as np

# Secuencia delta de inicio
#def secuencia04(n, x):
#    phi_nx = n/np.sqrt(np.pi) * np.exp(-n**2 * x**2)
#    return phi_nx

def derivada_secuencia04(n, x):
    der_phi_nx = - (2 * n**3) / np.sqrt(np.pi) * x * np.exp(-n**2 * x**2)
    return der_phi_nx

x = np.linspace(-3, 3, 200)

# Gráfica de la secuencia delta que ya está generada
#f1 = plt.figure()
#for i in [1,2,3]:
#    plt.plot(x, secuencia04(i, x), label="n = " + str(i))
    
#plt.title("Secuencia delta $\phi_{n}(x)$")    
#plt.legend(loc=1)


plt.plot(x, derivada_secuencia04(3, x))
plt.title("Derivada de la secuencia delta $\phi_{n}(x)$")
plt.axhline(y=0, lw=0.74, ls="dashed")
plt.axvline(x=0)
plt.legend(loc=1)
plt.show()