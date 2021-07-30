#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:58:29 2019

@author: gustavo
"""

import numpy as np
#import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

rc('lines', linewidth=0.5)



def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def Hermite(n, x):
    if n == 0:
        return 1
    
    hermite_v = [1, 2 * x]
    
    for m in range(2, n + 1):
        hermite_v.append(
            2 * x * hermite_v[m - 1] - 2 * (m - 1) * hermite_v[m - 2]
        )
        
    return hermite_v[n]

    
fig = plt.figure(figsize=(8, 6), frameon=False)
axs = fig.add_subplot('111')

X = np.linspace(-3, 3, 300)

for n in range(5):
    Y = [Hermite(n, x) for x in X]
    plt.plot(X, Y, label="$\mathcal{H}_{" + "{0}".format(n) + "}$")


axs.set_xlim(-3, 4)
axs.set_xlabel("$x$")
##axs.set_xlabel("$x$", fontproperties=plt.font_label)
#axs.set_xticks([x for x in range(-3,5)])
#axs.set_xticklabels(["${0}$".format(x) for x in range(-3,5)])
##axs.set_xticklabels(["${0}$".format(x) for x in range(-3,5)], fontproperties=plt.font_ticks)
#
#axs.set_ylim(-30, 30)
#axs.set_ylabel("$\mathcal{H}_n(x)$")
##axs.set_ylabel("$\mathcal{H}_n(x)$", fontproperties=plt.font_label)
#axs.set_yticks([x for x in range(-30,40,10)])
#axs.set_yticklabels(["${0}$".format(x) for x in range(-30,40,10)])
##axs.set_yticklabels(["${0}$".format(x) for x in range(-30,40,10)], fontproperties=plt.font_ticks)
#
#axs.set_title("$\mathrm{Polinomios\ de\ Hermite}$")
##axs.set_title("$\mathrm{Polinomios\ de\ Hermite}$", fontproperties=plt.font_title)

#plt.legend(loc=4)
#axs.legend(loc=4, prop=plt.font_legend)
#axs.grid('on')
#plt.tight_layout()
plt.show()
