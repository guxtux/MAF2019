#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:27:59 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

alpha = 1
t = np.linspace(0, 2*np.pi, num=1000)

x = alpha * np.sqrt(2) * np.cos(t) / (np.sin(t)**2 + 1)
y = alpha * np.sqrt(2) * np.cos(t) * np.sin(t) / (np.sin(t)**2 + 1)

plt.plot(x, y)
plt.axhline(y=0, lw=0.8, color='k')
plt.axvline(x=0, lw=0.8, color='k')
# Turn off tick labels
plt.gca().axes.get_yaxis().set_visible(False)
plt.gca().axes.get_xaxis().set_visible(False)
plt.show()