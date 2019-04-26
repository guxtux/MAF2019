#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:20:28 2019

@author: gustavo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_genlaguerre

a = 5.29*10**-11
numValues = 20000

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def R(n,l,r):

    '''Returns the radial wavefunction for each value of r where n is the principle quantum number and l is the angular momentum quantum number.'''
    y=np.zeros(numValues)
    #Generates an associated laguerre polynomial as a scipy.special.orthogonal.orthopoly1d
    Lag = eval_genlaguerre(n-l-1, 2*l+1)
    #Loops through each power of r in the laguerre polynomial and adds to the total
    for i in range(len(Lag)+1):
        i = float(i)
        #The main equation (What its all about)
        y = y + (((2*r/(n*a))**(l))*(np.exp(-r/(a*n)))*Lag[int(i)]*(((2*r)/(a*n))**i))
    return y


def plotPsi(r,psi):
    #plt.subplot(311)
    plt.plot(r, psi, color = 'black')
    plt.grid(True)
    plt.xlabel("r/a (m)")
    plt.ylabel("$R_{n \ell}(r)$")
    plt.title('Funciones radiales de onda $R_{n \ell}(r)$')
    plt.xlim((0,15))


def main():
    numPsi = int(input("How many wavefunctions do you want to draw?"))
    #Note that the whole wavefunction should be drawn or the normalise function will not work correctly
    width = float(input("To what value of r (in units of a) do you want to plot?")) * a
    print("1: Plot the wavefunction")
    print("2: Plot the wavefunction squared (the probability density)")
    print("3: Plot the wavefunction squared times pi r^2 (the radial distribution function)")
    print("4: Plot all 3")
    choice = int(input("Choose an option:"))
    for i in range(numPsi):
        print("Wavefunction " + str(i+1))
        n = float(input("Enter n:"))
        l = float(input("Enter l:"))
        r = np.linspace(0,width, numValues)
        psi = R(n,l,r)

        #Converts r into units of a
        r = r/a
        #psi = normalise(r, psi)
        
        plotPsi(r, psi)
    plt.show()


if __name__ == '__main__':
    main()