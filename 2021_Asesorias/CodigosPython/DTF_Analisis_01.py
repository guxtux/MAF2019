# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:20:38 2021

@author: gusto
"""

import numpy as np
import scipy.fftpack as fourier


xn = [0, 1, 2, 3, 4] # Definimos una función en tiempo discreto
Xk = fourier.fft(xn) # Calculamos la FFT
print('DFT: ', Xk)

M_Xk = abs(Xk)                   # Calculamos la Magnitud de la FFT
Ph_Xk = np.angle(Xk)             # Calculamos la Fase de la FFT
print('Magnitud: ', M_Xk)
print('Angulo: ', Ph_Xk*180/np.pi)

