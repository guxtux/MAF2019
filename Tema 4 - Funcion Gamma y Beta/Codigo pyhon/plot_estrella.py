#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:05:57 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 20.
c = 1.
t = np.linspace(-1, 1, 500)

def y1(x):
    return (1 - x**(b/c))**(c/b)

def y2(x):
    return -(1 - x**(b/c))**(c/b)

def primerCuadrante(t):
    plt.plot(t, y1(t), color='k')
    
def todosCuadrantes(t):
    primerCuadrante(t)
    plt.plot(t, y2(t), color='k')
    plt.plot(-y1(t), t, color='k')
    plt.plot(y2(t), -t, color='k')
    plt.title('Curva $x^{20} + y^{20} = a^{20}$')
    
def ejesGrafica():
    plt.axhline(y=0, lw=0.8, color='k')
    plt.axvline(x=0, lw=0.8, color='k')
    # Turn off tick labels
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gca().axes.get_xaxis().set_visible(False)
    
def cuadranteGrafica():
    primerCuadrante
    plt.fill_between(t, 0, y1(t), alpha=0.5)
    plt.title('Primer cuadrante para la curva $x^{20} + y^{20} = a^{20}$')
    plt.text(0.15, 0.25, "R", fontsize="20")

plt.figure(1)
todosCuadrantes(t)
ejesGrafica()

plt.figure(2)
primerCuadrante(t)
ejesGrafica()
cuadranteGrafica()


plt.show()
