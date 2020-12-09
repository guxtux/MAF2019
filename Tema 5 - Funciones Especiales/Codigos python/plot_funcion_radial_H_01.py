#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import n, l, r, Z
from sympy.physics import hydrogen
from sympy.utilities.lambdify import lambdify

R_nl = lambdify((n, l, r, Z), hydrogen.R_nl(n, l, r, Z), ('numpy', 'math', 'sympy'))

Z = 1
n, l = 2, 0
r = np.linspace(0, 10, 1000)

plt.plot(r, R_nl(n, l, r, Z))
plt.show()