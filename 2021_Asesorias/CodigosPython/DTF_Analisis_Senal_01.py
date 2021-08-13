# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:05:41 2021

@author: gusto
"""

import numpy as np
import scipy.fftpack as fourier
import matplotlib.pyplot as plt

def ejesGrafica():
    plt.xlabel('Tiempo (s)', fontsize='14')
    plt.ylabel('Amplitud', fontsize='14')
    plt.show()


Ts = 0.001               
n = Ts*np.arange(0, 1000)
                        # Definimos un tiempo y frecuencia de muestreo
Fs=1/Ts
w1 = 2*np.pi*60                                  # Definimos una frecuencia de 60 Hz para la señal 1
w2 = 2*np.pi*223                                 # Definimos una frecuencia de 223 Hz para la señal 2

x1 = 3*np.sin(w1*n)
x2 = 2.3*np.sin(w2*n) 
ruido = np.random.random(len(n))
x = x1 + x2 +ruido        # Construimos una señal compuesta por la señal 1 y 2, y agregamos ruido

plt.figure(1)
plt.plot(n, x1)
plt.title("Señal $w1 = 3 \, \cos(2 \, \pi * 60 \, t)$")
ejesGrafica()


plt.figure(2)
plt.plot(n, x2)
plt.title("Señal $w2 = 3 \, \cos(2 \, \pi * 223 \, t)$")
ejesGrafica()


plt.figure(3)
plt.plot(n, x,'.-')
plt. title("La suma de las dos señal más el ruido")
ejesGrafica()


gk = fourier.fft(x)                             # Calculamos la FFT
M_gk = abs(gk)                                  # Calculamos la Magnitud de la FFT

F = Fs*np.arange(0, len(x))/len(x)              # Definimos el Vector de Frecuencias

plt.figure(4)
plt.plot(F, M_gk, color="red")
plt.xlabel('Frecuencia (Hz)', fontsize='14')
plt.ylabel('Amplitud FFT', fontsize='14')
plt.title("Espectro de frecuencias luego de usar la FFT")
plt.xlim(0,1000)
plt.show()