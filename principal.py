#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:53:36 2020

@author: Lauría Juan

Módulo principal.
Procesamiento digital de señales.
19/08 - 1er clase (uso de generador de señales)
26/08 - 2da clase (uso de transformada discreta)
02/09 - 3er clase (analizador de espectro)
"""

import matplotlib.pyplot as plt
import numpy as npy
import scipy as spy

import senoidalTest as fxSen
import analizador as fxEsp

vmax = 1
dc = 0
fs = 500
N = 500
ph = npy.pi * 0
f = 10

  
tt,xx = fxSen.mi_func_sen(vmax,dc,f,ph,N,fs)  
tt2,xx2 = fxSen.mi_func_sen(vmax/2,dc,3*f,ph,N,fs)  
#ff = npy.linspace(0, (N-1)*fs/N, N)

modulo,fase = fxEsp.mi_analizador(xx+xx2,fs,N)

# Para chequear usando la función FFT

# fft = npy.fft.fft(xx)
# modulo = npy.abs(fft)
# fase = npy.angle(fft)

tt = npy.arange(N/fs, step=1/fs)

plt.figure(1)
plt.subplot(121)
ploteo1 = plt.plot(fs*tt[:N // 2],modulo[:N // 2])
plt.title('Modulo')
plt.xlabel('Frecuencia(Hz)')
plt.ylabel('Amplitud')
plt.grid()
plt.subplot(122)
ploteo1 = plt.plot(fs*tt[:N // 2],fase[:N // 2])
plt.title('Fase')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Fase')
plt.grid()
plt.show()


