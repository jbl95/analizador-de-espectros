#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 23:29:27 2020

@author: Lauría Juan

Generador de Ruido.
Procesamiento digital de señales.
"""

import numpy as npy

def mi_func_ruido (var,fs, N):
    
    xx = npy.sqrt(var) * npy.random.randn(N,1)
    tt = npy.arange(N/fs, step=1/fs)    
    return tt,xx