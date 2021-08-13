# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:20:38 2021

@author: gusto
"""

import numpy as np
import scipy.fftpack as fourier


gn = [0, 1, 2, 3, 4] # Definimos una función en tiempo discreto
gk = fourier.fft(gn) # Calculamos la FFT
gk

M_gk = abs(gk)                   # Calculamos la Magnitud de la FFT
Ph_gk = np.angle(gk)             # Calculamos la Fase de la FFT
print('Magnitud: ', M_gk)
print('Angle: ',Ph_gk*180/np.pi)

