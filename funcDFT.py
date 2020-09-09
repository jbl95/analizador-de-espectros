#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:16:48 2020

@author: Lauría Juan

Transformada discreta de Fourier - Módulo de función.
Procesamiento digital de señales.
26/08 - 2da clase

"""

import numpy as npy

def mi_func_DFT (xx,nn):
    
    xx_dft = npy.zeros(nn,dtype=complex)
    
    aprox = nn
    
    for k in range(nn):
            for n in range(aprox):
                xx_dft[k] = xx_dft[k] + (xx[n] * npy.exp((-2) * 1j * npy.pi * k * n / nn))
            
    return xx_dft