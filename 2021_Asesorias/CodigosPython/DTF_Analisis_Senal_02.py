# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy.fftpack as fourier
import matplotlib.pyplot as plt


def pieGrafica():
    plt.xlabel('Tiempo (s)', fontsize='14')
    plt.ylabel('Amplitud', fontsize='14')
    plt.show()


Ts = 0.001                        # Definimos un tiempo y frecuencia de muestreo
Fs = 1/Ts
n = Ts*np.arange(0, 1000)

w1 = 3*np.sin(2*np.pi*60*n)       # Definimos una frecuencia de 60 Hz para la señal 1
w2 = 2.3*np.sin(2*np.pi*223*n)    # Definimos una frecuencia de 223 Hz para la señal 2

ruido = np.random.random(len(n))
xn = w1 + w2 + ruido              # Construimos una señal compuesta por la señal 1 y 2,
                                  # agregamos ruido

plt.figure(1)
plt.plot(n, w1)
plt.title('Gráfica de la señal $w_{1} = 3 \cos (2 \pi * 60 t)$')
pieGrafica()

plt.figure(2)
plt.plot(n, w2)
plt.title('Gráfica de la señal $w_{1} = 2.3 \cos (2 \pi * 223 t)$')
pieGrafica()

plt.figure(3)
plt.title('Gráfica de la señal compuesta $w_{1} + w_{2} +$ ruido')
plt.plot(n, xn,'.-')
pieGrafica()


Xk = fourier.fft(xn)             # Calculamos la FFT
M_Xk = abs(Xk)                   # Calculamos la Magnitud de la FFT

F = Fs*np.arange(0, len(xn))/len(xn)   # Definimos el Vector de Frecuencias

plt.figure(2)
plt.plot(F, M_Xk, color='red')
plt.xlabel('Frecuencia (Hz)', fontsize='14')
plt.ylabel('Amplitud FFT', fontsize='14')
plt.title('Espectro de frecuencias obtenido con la DFT')
plt.show()