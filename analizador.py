#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 23:00:10 2020

@author: Lauría Juan

Analizador de espectro - Módulo y fase.
Procesamiento digital de señales.
02/09 - 3er clase

"""

import numpy as npy
import funcDFT as fxDFT

def mi_analizador (senial,fs,N):
    
    senial_DFT = fxDFT.mi_func_DFT(senial,N)
    
    modulo = npy.abs(senial_DFT) 
    fase = npy.angle (senial_DFT) 
    
    return modulo,fase
    