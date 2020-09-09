#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 23:29:27 2020

@author: Lauría Juan

Generador de Ruido.
Procesamiento digital de señales.
"""

import numpy as npy
import senoidalTest as fxSen
import matplotlib.pyplot as plt

def mi_func_ruido (var,fs, N):
    
    xx = npy.sqrt(var) * npy.random.randn(N,1)
    tt = npy.arange(N/fs, step=1/fs)    
    return tt,xx


tiempo,senial = mi_func_ruido(0.1, 500, 500)

tt_s, xx_s = fxSen.mi_func_sen(1,0,1,0,500,500)

xx_s = xx_s.reshape((500,1))

suma = senial + xx_s

plt.plot(tt_s,suma)
