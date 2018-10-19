#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:35:48 2018

@author: gustavo
"""

from sympy.utilities.lambdify import implemented_function
from sympy.physics.hydrogen import R_nl
a, r = symbols('a r')
psi_nl = implemented_function('psi_nl', Lambda([a, r], R_nl(1, 0, a, r)))
psi_nl(a, r)